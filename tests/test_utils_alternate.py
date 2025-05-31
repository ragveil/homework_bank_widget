from typing import Any
from unittest.mock import mock_open, patch

from src.utils_alternate import get_transactions_csv, get_transactions_xls


def test_get_transactions_csv_correct(csv_sample: str, csv_result: list[dict[str, str]]) -> None:
    with patch("builtins.open", mock_open(read_data=csv_sample)) as mock_file:
        assert get_transactions_csv("builtins.open") == csv_result
        mock_file.assert_called_once_with("builtins.open", encoding="UTF-8")


def test_get_transactions_csv_decode_error(wrong_csv: list[dict[str, str | int]]) -> None:
    with patch("builtins.open", mock_open(read_data=str(wrong_csv))) as mock_file:
        assert get_transactions_csv("builtins.open") == []
        mock_file.assert_called_once_with("builtins.open", encoding="UTF-8")


def test_get_transactions_csv_no_file() -> None:
    assert get_transactions_csv("wrong_path") == []


@patch("pandas.read_excel")
def test_get_transactions_xls_correct(mock_excel: Any, xls_out: list[dict[str, str | int]]) -> None:
    mock_excel.return_value.to_dict.return_value = xls_out
    assert get_transactions_xls("some_path") == xls_out
    mock_excel.assert_called_once_with("some_path")


def test_get_transactions_xls_no_file() -> None:
    assert get_transactions_xls("wrong_path") == []
