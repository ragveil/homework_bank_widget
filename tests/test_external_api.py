from typing import Any

import pytest
import requests
from pytest_mock import MockFixture

from src.external_api import get_rub_transactions


def test_get_rub_transactions_usd(mocker: MockFixture, usd_conversion: dict[str, Any]) -> None:
    mock_response = mocker.patch("requests.get")
    mock_response.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1747777395, "rate": 80.624798},
        "date": "2025-05-20",
        "result": 662846.295533,
    }
    assert get_rub_transactions(usd_conversion) == 662846.295533
    mock_response.assert_called_once()


def test_get_rub_transactions_eur(mocker: MockFixture, eur_conversion: dict[str, Any]) -> None:
    mock_response = mocker.patch("requests.get")
    mock_response.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 9824.07},
        "info": {"timestamp": 1747791437, "rate": 91.000365},
        "date": "2025-05-21",
        "result": 893993.955786,
    }
    assert get_rub_transactions(eur_conversion) == 893993.955786
    mock_response.assert_called_once()


def test_get_rub_transactions_eur_err(mocker: MockFixture, bubble_conversion: dict[str, Any]) -> None:
    mock_response = mocker.patch("requests.get", side_effect=requests.exceptions.ConnectionError)
    assert get_rub_transactions(bubble_conversion) == "Ошибка обращения к api"
    mock_response.assert_called_once()


def test_get_rub_transactions_rub(rub_conversion: dict[str, Any]) -> None:
    assert get_rub_transactions(rub_conversion) == 31957.58


@pytest.mark.parametrize(
    "operation, expected",
    [
        ({}, "'operationAmount': Отсутствует значение о сумме операции или валюте."),
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб."}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            "'code': Отсутствует значение о сумме операции или валюте.",
        ),
    ],
)
def test_get_rub_transactions(operation: dict[str, Any], expected: str) -> None:
    assert get_rub_transactions(operation) == expected
