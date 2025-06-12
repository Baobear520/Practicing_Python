"""
User Story #1: Как пользователь, я хочу искать свободные номера в отеле, подходящие мне по параметрам:
    Дата заезда.
    Дней пребывания в отеле.
    Количество человек.
    Верхняя граница общей стоимости (бюджет)
    Некоторые удобства в комнате: wifi, ac, tv
"""

import pytest
from typing import Set, List
from datetime import date, timedelta
from enum import Enum
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Amenity(str, Enum):
    wifi = "wifi"
    ac = "ac"
    tv = "tv"


@dataclass
class SearchRequest:
    date_from: date
    days: int
    guests: int
    budget: int
    amenities: Set[Amenity]


@dataclass
class Booking:
    from_date: date
    to_date: date

@dataclass
class DateRange:   #helper class
    from_date: date
    to_date: date

    def overlaps(self, other: 'DateRange') -> bool:
        return self.from_date < other.to_date and self.to_date > other.from_date

@dataclass
class Room:
    id: int
    price: int
    capacity: int
    amenities: Set[Amenity]
    bookings: List[Booking]


@dataclass
class User:
    id: int
    name: str
    email: str


class RoomRepository(ABC):
    @abstractmethod
    async def find_rooms_by_request(self, request: SearchRequest) -> List[Room]:
        pass


class SearchService(ABC):
    @abstractmethod
    async def find_by_request(self,request: SearchRequest) -> List:
        pass

class CheckRoomBookings:
    @staticmethod
    def is_available(room: Room, request: SearchRequest) -> bool:
        request_range = DateRange(
            from_date=request.date_from,
            to_date=request.date_from + timedelta(days=request.days)
        )
        return not any(
            request_range.overlaps(DateRange(booking.from_date,booking.to_date)) #checking if no booking overlaps with the request
            for booking in room.bookings
        )


class SearchRoomService(SearchService):
    def __init__(self, room_repository: RoomRepository, checker: CheckRoomBookings):
        self._room_repository = room_repository
        self._checker = checker


    async def find_by_request(self, request: SearchRequest)-> List[Room]:
        filtered_rooms = await self._room_repository.find_rooms_by_request(request)
        return [room for room in filtered_rooms if self._checker.is_available(room,request)]  #applying business logic


class InMemoryRoomRepository(RoomRepository):  #filtering
    def __init__(self, rooms):
        self._rooms = rooms

    async def find_rooms_by_request(self, request: SearchRequest) -> List[Room]:
        return [room for room in self._rooms if room.capacity >= request.guests \
                and request.amenities.issubset(room.amenities) \
                and room.price <= request.budget
                ]



@pytest.mark.asyncio
async def test_that_there_are_rooms_available_for_given_request():
    room_1 = Room(
        id=1,
        price=10_000,
        capacity=2,
        amenities={Amenity.wifi, Amenity.ac},
        bookings=[
            Booking(from_date=date(2024, 1, 1), to_date=date(2024, 2, 1)),
            Booking(from_date=date(2024, 2, 12), to_date=date(2024, 2, 15)),
            Booking(from_date=date(2024, 2, 20), to_date=date(2024, 2, 28)),
        ],
    )
    room_2 = Room(
        id=2,
        price=10_000,
        capacity=2,
        amenities={Amenity.wifi, Amenity.ac,Amenity.tv},
        bookings=[
            Booking(from_date=date(2024, 1, 1), to_date=date(2024, 2, 1)),
            Booking(from_date=date(2024, 2, 12), to_date=date(2024, 2, 15)),
            Booking(from_date=date(2024, 2, 20), to_date=date(2024, 2, 28)),
        ],
    )
    room_repository = InMemoryRoomRepository([room_1, room_2])
    checker = CheckRoomBookings()
    search_service = SearchRoomService(room_repository,checker)

    assert (
        await search_service.find_by_request(
            request=SearchRequest(
                date_from=date(2024, 2, 1),
                days=10,
                guests=2,
                budget=1_000_000,
                amenities={Amenity.wifi, Amenity.ac, Amenity.tv},
            )
        )
        != []
    )












