import random
from typing import List, Tuple, Optional


class Card:
    """Класс, представляющий игральную карту."""

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f'{self.rank} of {self.suit}'

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


class Deck:
    """Класс, представляющий колоду карт."""

    RANKS: Tuple[str, ...] = (
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King', 'Ace'
    )
    SUITS: Tuple[str, ...] = (
        'Hearts', 'Spades', 'Diamonds', 'Clubs'
    )

    def __init__(self, full_deck: bool = True) -> None:
        self.full_deck = full_deck
        self.cards: List[Card] = []
        self._initialize_deck()

    def _initialize_deck(self) -> None:
        """Инициализирует колоду карт."""
        ranks = self.RANKS if self.full_deck else self.RANKS[4:]
        self.cards = [Card(rank, suit) for rank in ranks for suit in self.SUITS]
        self._shuffle()

    def _shuffle(self) -> None:
        """Перемешивает колоду."""
        random.shuffle(self.cards)

    def draw(self) -> Card:
        """Возвращает случайную карту из колоды и удаляет её из колоды."""
        if not self.cards:
            raise ValueError("Колода пуста")
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

    def __len__(self) -> int:
        """Возвращает количество оставшихся карт в колоде."""
        return len(self.cards)

    def __repr__(self) -> str:
        return f'Deck(cards={len(self.cards)})'


class Hand:
    def __init__(self,max_num):
        self.max_number_of_cards = max_num
        self.cards = []

    def add_card(self, new_card):
        if self.cards == [] or len(self.cards) < self.max_number_of_cards:
            self.cards.append(new_card)
        else:
            print("Не могу добавить карту: достигнут максимум для одного игрока!")


# Пример использования
if __name__ == "__main__":
    deck = Deck()
    print(f"Колода создана: {deck}")
    print()
    player = Hand(3)
    try:
        for n in range(player.max_number_of_cards):
            card = deck.draw()
            print(f"Вытянута карта: {card}")
            player.add_card(card)
            print(f"Осталось карт в колоде: {len(deck)}")
            print(f"Количество карт на руке: {len(player.cards)}")
            print(f"Карты на руке: {player.cards}")

    except ValueError as e:
        print(e)