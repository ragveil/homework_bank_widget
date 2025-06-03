from typing import Any


def filter_by_state(list_of_dicts: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """
    Выводит данные в соответствии с состоянием операции.
    :param list_of_dicts: Входящее значение в виде списка словарей.
    :param state: Значение для фильтрации по умолчанию, строка.
    :return: Список словарей, соответствующих критерию фильтрации.
    """
    if any(d.get("state") == state for d in list_of_dicts):
        return list(filter(lambda d: d.get("state") == state, list_of_dicts))
    else:
        new_transactions = []
        for d in list_of_dicts:
            if len(d) != 0:
                new_transactions.append(d)
        print(f"Статус {state} отсутствует в списке транзакций. Возвращаю исходные транзакции.")
        return new_transactions


def sort_by_date(list_of_dicts: Any, sort: bool = True) -> Any:
    """
    Сортирует операции в соответствующем порядке.
    :param list_of_dicts: Входящее значение в виде списка словарей.
    :param sort: Значение для сортировки по умолчанию типа bool.
    :return: Список словарей, отсортированных в указанном порядке.
    """
    if any(d.get("date") for d in list_of_dicts):
        return sorted(list_of_dicts, key=lambda d: str(d.get("date")), reverse=sort)
    else:
        return "Неверный формат данных"
