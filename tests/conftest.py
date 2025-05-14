import pytest


@pytest.fixture
def card_number() -> str:
    return "5999414228426353"


@pytest.fixture
def account_number() -> str:
    return "73654108430135874305"


@pytest.fixture
def date() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def processing_data() -> list[dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def processing_data_wrong() -> list[dict[str, str | int]]:
    return [
        {"id": 41428829, "states": "NOTHING", "dates": "2019-07-038:35:29.512364"},
        {"id": 939719570, "states": "NOTHING", "dates": "2018-06-3002:08:58.425572"},
        {"id": 594226727, "states": "NOTHING", "dates": "2018-09-1221:27:25.241689"},
        {"id": 615064591, "states": "NOTHING", "dates": "2018-10-1408:21:33.419441"},
    ]


@pytest.fixture
def summ_num_correct() -> str:
    return (
        "Начало выполнения функции: 2025-05-08 14:00:00\n"
        "Выполняемая функция: summ_num\n"
        "Переданные аргументы:\n"
        "2 позиционных (1, 2)\n"
        "0 именованных \n"
        "Окончание работы функции: 2025-05-08 14:00:00\n"
        "Результат работы функции: 3\n"
        "Время работы функции: 0.0ms.\n"
    )


@pytest.fixture
def zero_division_err() -> str:
    return (
        "Время возникновения ошибки: 2025-05-08 14:00:00\n"
        "Сбой функции zero_division. Ошибка ZeroDivisionError\n"
        "Переданные аргументы:\n"
        "2 позиционных (1, 0)\n"
        "0 именованных \n"
        "\n"
    )
