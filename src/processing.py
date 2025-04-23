from typing import Any


def filter_by_state(list_of_dicts: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """
    Выводит данные в соответствии с состоянием.
    :param list_of_dicts: Входящее значение в виде списка словарей.
    :param state: Значение для фильтрации по умолчанию, строка.
    :return: Список словарей, соответствующих критерию фильтрации.
    """
    return list(filter(lambda d: d.get("state") == state, list_of_dicts))


def sort_by_date(list_of_dicts: list[dict[str, Any]], sort: bool = True) -> list[dict[str, str | int]] | None:
    """
    Сортирует операции в соответствующем порядке.
    :param list_of_dicts: Входящее значение в виде списка словарей.
    :param sort: Значение для сортировки по умолчанию типа bool.
    :return: Список словарей, отсортированных в указанном порядке.
    """
    return sorted(list_of_dicts, key=lambda d: str(d.get("date")), reverse=sort)
