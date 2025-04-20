def filter_by_state(list_of_dicts: list[dict[str, int | str]], state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """
    Выводит данные в соответствии с состоянием.
    :param list_of_dicts: Входящее значение в виде списка словарей.
    :param state: Значение для фильтрации по умолчанию, строка.
    :return: Список словарей, соответствующих критерию фильтрации.
    """
    return list(filter(lambda d: d.get("state") == state, list_of_dicts))
