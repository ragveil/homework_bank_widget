import pytest

from src.main import BANKING_OPERATIONS
from src.processing import filter_by_state, sort_by_date

WRONG_RESULT = "Неверный формат данных"


def test_filter_and_sorting_correct(processing_data: list[dict[str, str | int]]) -> None:
    """
    Тестируем функции filter_by_state и sort_by_date с использованием корректных данных и значением по умолчанию.
    В данном тесте используется фикстура.
    :param processing_data: Входные данные, список словарей.
    :return: Результат работы теста.
    """
    assert filter_by_state(processing_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(processing_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "data, arg, expected",
    [
        (
            BANKING_OPERATIONS,
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            BANKING_OPERATIONS,
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            BANKING_OPERATIONS,
            "RANDOM TEXT",
            WRONG_RESULT,
        ),
        (
            BANKING_OPERATIONS,
            None,
            WRONG_RESULT,
        ),
        (
            BANKING_OPERATIONS,
            "",
            WRONG_RESULT,
        ),
    ],
)
def test_filter_params(data: list[dict[str, str | int]], arg: str, expected: list[dict[str, str | int]]) -> None:
    """
    Тестируем функцию filter_by_state с использованием дополнительных аргументов.
    В данном тесте используется параметризация.
    :param data: Входные данные, список словарей.
    :param arg: Входные данные, параметры 'EXECUTED' и 'CANCELED'.
    :param expected: Ожидаемый результат, список словарей.
    :return: Результат работы теста.
    """
    assert filter_by_state(data, arg) == expected


@pytest.mark.parametrize(
    "data, arg, expected",
    [
        (
            BANKING_OPERATIONS,
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            BANKING_OPERATIONS,
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            BANKING_OPERATIONS,
            None,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            BANKING_OPERATIONS,
            "RANDOM TEXT",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            BANKING_OPERATIONS,
            " ",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            BANKING_OPERATIONS,
            "",
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sorting_params(data: list[dict[str, str | int]], arg: bool, expected: list[dict[str, str | int]]) -> None:
    """
    Тестируем функцию sort_by_date с использованием дополнительных аргументов:
    True - Равно значению по умолчанию, ожидается сортировка в порядке убывания;
    False - Ожидается сортировка в порядке возрастания;
    None - Равнозначно False, ожидается сортировка в порядке возрастания;
    'RANDOM TEXT' - Равнозначно True, ожидается сортировка в порядке убывания;
    ' ' - Равнозначно True, поскольку строка не пуста, ожидается сортировка в порядке убывания;
    '' - Равнозначно False, поскольку строка пуста, ожидается сортировка в порядке возрастания.
    В данном тесте используется параметризация.
    :param data: Входные данные, список словарей.
    :param arg: Входные данные, параметры True и False.
    :param expected: Ожидаемый результат, список словарей.
    :return: Результат работы теста.
    """
    assert sort_by_date(data, arg) == expected


def test_filter_and_sorting_wrong(processing_data_wrong: list[dict[str, str | int]]) -> None:
    """
    Тестируем функции filter_by_state и sort_by_date с использованием некорректных данных.
    В данном тесте используется фикстура.
    :param processing_data_wrong: Входные данные в виде списка словарей. Значения для ключей заданы неверно.
    :return: Результат работы теста.
    """
    assert filter_by_state(processing_data_wrong) == WRONG_RESULT
    assert sort_by_date(processing_data_wrong) == WRONG_RESULT
    assert filter_by_state([]) == WRONG_RESULT
    assert sort_by_date([]) == WRONG_RESULT
