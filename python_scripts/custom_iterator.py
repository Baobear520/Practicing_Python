from collections.abc import Iterable, Iterator
from typing import Optional, IO


class MyIter:
    def __init__(self,maximum):
        self.maximum = maximum
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.maximum:
            self.current += 1
            return self.current
        raise StopIteration


a = MyIter(3)
for i in a:
    print(i)


#Более универсальный класс

class CustomIterator:
    """
    Кастомный итератор для работы с коллекциями и потоками.

    Args:
        iterable (Iterable, optional): Итерируемый объект (список, кортеж и т.д.).
        stream (IO, optional): Поток с методом read (например, файловый объект).
        chunk_size (int, optional): Размер чанка для чтения из потока. По умолчанию 1024.

    Raises:
        ValueError: Если не передан ни iterable, ни stream.
        ValueError: Если stream не имеет метода read.
    """

    def __init__(
        self,
        iterable: Optional[Iterable] = None,
        stream: Optional[IO] = None,
        chunk_size: int = 1024
    ):
        if iterable is not None:
            self._iterator = iter(iterable)
        elif stream is not None:
            if not hasattr(stream, "read"):
                raise ValueError("Stream должен иметь метод 'read'.")
            self.stream = stream
            self.chunk_size = chunk_size
        else:
            raise ValueError("Должен быть передан iterable или stream.")

    def __iter__(self) -> Iterator:
        return self

    def __next__(self):
        if hasattr(self, "_iterator"):
            return next(self._iterator)  # Стандартная итерация
        elif hasattr(self, "stream"):
            chunk = self.stream.read(self.chunk_size)
            if not chunk:
                raise StopIteration
            return chunk
        raise StopIteration


# Пример использования с коллекцией
my_iterable = (1, 2, 3)
iterator = CustomIterator(iterable=my_iterable)
for item in iterator:
    print(item)  # 1, 2, 3

# Пример использования с потоком
with open('/Users/aldmikon/Desktop/phrases.txt', 'r') as stream:
    iterator = CustomIterator(stream=stream, chunk_size=64)
    for chunk in iterator:
        print(chunk)