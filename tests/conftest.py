from typing import Any

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


@pytest.fixture
def json_sample() -> list[dict[str, Any]]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


@pytest.fixture
def wrong_json_list() -> str:
    return "{'name': 'John', 'age': 30, 'city': 'New York'}"


@pytest.fixture
def rub_conversion() -> dict[str, Any]:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def usd_conversion() -> dict[str, Any]:
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@pytest.fixture
def eur_conversion() -> dict[str, Any]:
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def bubble_conversion() -> dict[str, Any]:
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "BUBBLE", "code": "BUBBLE"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
