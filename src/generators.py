from collections.abc import Generator, Iterator
from typing import Any


def filter_by_currency(b_data: list[dict[str, Any]], curr: str) -> Iterator[Any]:
    """
    Итератор для работы со списком словарей, находит нужные словари по указанному значению кода валюты.
    :param b_data: Входное значение, список словарей.
    :param curr: Ключевое значение для фильтрации, строка.
    :return: Ленивый объект, итератор.
    """
    return filter(lambda item: item.get("operationAmount")["currency"]["code"] == curr.upper(), b_data)


def transaction_descriptions(b_data: list[dict[str, Any]]) -> Generator[Any]:
    """
    Выводит информацию о типе проводимых транзакциях построчно.
    :param b_data: Входное значение, список словарей.
    :return: Генератор (информация о типе транзакций).
    """
    for item in b_data:
        yield item.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """
    Генерирует номера карт формата 'XXXX XXXX XXXX XXXX'.
    :param start: Стартовая позиция генератора, цифровое значение 'от' (включительно).
    :param stop: Конечная позиция генератора, цифровое значение 'до' (не включая).
    :return: Ленивый объект, генератор (номера карт).
    """
    if 0 >= start or stop > 10000000000000000:
        raise ValueError("Некорректные значения для генерации номера карты")
    if start >= stop:
        raise ValueError("Неверно заданы стартовое и конечное значение")
    for num in range(start, stop):
        card_num = str(num).zfill(16)
        result_num = f"{card_num[0:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:16]}"
        yield result_num
