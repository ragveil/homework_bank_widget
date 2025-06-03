import re
from collections import Counter
from typing import Any


def search_item(operations: list[dict[str, int | str]] | str, keyword: str) -> Any:
    """
    Функция для поиска транзакций по ключевому слову.
    :param operations: Входные данные, список словарей.
    :param keyword: Ключевое слово для поиска, строка.
    :return: Список найденных транзакций, список словарей.
    """
    keyword = keyword.lower()
    result_operations = []
    for operation in operations:
        if re.search(keyword, str(operation).lower()) is not None:
            result_operations.append(operation)
        else:
            pass
    if len(result_operations) == 0:
        print("Совпадений не найдено, будет возвращен исходный список транзакций")
        return operations
    else:
        return result_operations


def count_categories(operations: list[dict[str, str | int]], cat: list[str]) -> dict[Any, int]:
    """
    Функция для подсчета категорий транзакций.
    :param operations: Входные данные, список словарей.
    :param cat: Категории для подсчета, список.
    :return: Результат работы функции, словарь формата "Название категории" : "Количество совпадений"
    """
    categories_list = []
    for operation in operations:
        if len(operation) != 0 and operation.get("description") in cat:
            categories_list.append(operation.get("description"))
    result = dict(Counter(categories_list))
    return result
