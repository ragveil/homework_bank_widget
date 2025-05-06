from collections.abc import Iterator
from typing import Any


def filter_by_currency(b_data: list[dict[str, Any]], curr: str) -> Iterator[Any]:
    """
    Итератор для работы со списком словарей, находит нужные словари по указанному значению кода валюты.
    :param b_data: Входное значение, список словарей.
    :param curr: Ключевое значение для фильтрации, строка.
    :return: Ленивый объект, итератор.
    """
    return filter(lambda item: item.get("operationAmount")["currency"]["code"] == curr.upper(), b_data)
