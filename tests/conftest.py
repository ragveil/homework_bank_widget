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


@pytest.fixture
def csv_sample() -> str:
    return """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 664561298323391;Счет 660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 01889670065;Discover 28384694643;Перевод с карты на карту
593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 32722494097;Visa 19550473710;Перевод с карты на карту
366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;Discover 55596714937;Visa 88829287420;Перевод с карты на карту"""


@pytest.fixture
def csv_result() -> list[dict[str, str]]:
    return [
        {
            "amount": "16210",
            "currency_code": "PEN",
            "currency_name": "Sol",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 664561298323391",
            "id": "650703",
            "state": "EXECUTED",
            "to": "Счет 660563456619397",
        },
        {
            "amount": "29740",
            "currency_code": "COP",
            "currency_name": "Peso",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 01889670065",
            "id": "3598919",
            "state": "EXECUTED",
            "to": "Discover 28384694643",
        },
        {
            "amount": "30368",
            "currency_code": "TZS",
            "currency_name": "Shilling",
            "date": "2023-07-22T05:02:01Z",
            "description": "Перевод с карты на карту",
            "from": "Visa 32722494097",
            "id": "593027",
            "state": "CANCELED",
            "to": "Visa 19550473710",
        },
        {
            "amount": "29482",
            "currency_code": "IDR",
            "currency_name": "Rupiah",
            "date": "2020-08-02T09:35:18Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 55596714937",
            "id": "366176",
            "state": "EXECUTED",
            "to": "Visa 88829287420",
        },
    ]


@pytest.fixture
def wrong_csv() -> str:
    return "{'name': 'John', 'age': 30, 'city': 'New York'}"


@pytest.fixture
def xls_out() -> list[dict[str, str | float]]:
    return [
        {
            "amount": 16210.0,
            "currency_code": "PEN",
            "currency_name": "Sol",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "id": 650703.0,
            "state": "EXECUTED",
            "to": "Счет 39745660563456619397",
        },
        {
            "amount": 29740.0,
            "currency_code": "COP",
            "currency_name": "Peso",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "id": 3598919.0,
            "state": "EXECUTED",
            "to": "Discover 0720428384694643",
        },
    ]
