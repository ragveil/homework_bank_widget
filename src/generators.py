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
