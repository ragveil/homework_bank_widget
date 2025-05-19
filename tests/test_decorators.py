from typing import Any

import pytest
from freezegun import freeze_time

from src.constants import PATH_TO_LOGS
from src.decorators import log


def test_summ_num_correct(capsys: Any, summ_num_correct: str) -> None:
    @freeze_time("2025-05-08 04:00:00")
    @log()
    def summ_num(a: int, b: int) -> int:
        return a + b

    summ_num(1, 2)
    captured = capsys.readouterr()
    assert summ_num_correct == captured.out


def test_summ_num_correct_txt(summ_num_correct: str) -> None:
    @freeze_time("2025-05-08 04:00:00")
    @log("summ_num.txt")
    def summ_num(a: int, b: int) -> int:
        return a + b

    summ_num(1, 2)
    with open(PATH_TO_LOGS + "summ_num.txt", "r", encoding="UTF-8", newline="\n") as f:
        log_file = f.read()
        assert summ_num_correct == log_file


def test_zero_division(capsys: Any, zero_division_err: str) -> None:
    @freeze_time("2025-05-08 04:00:00")
    @log()
    def zero_division(a: int, b: int) -> float:
        return a / b

    zero_division(1, 0)
    captured = capsys.readouterr()
    assert zero_division_err == captured.out


def test_zero_division_txt(zero_division_err: str) -> None:
    @freeze_time("2025-05-08 04:00:00")
    @log("zero_division.txt")
    def zero_division(a: int, b: int) -> float:
        return a / b

    zero_division(1, 0)
    with open(PATH_TO_LOGS + "zero_division.txt", "r", encoding="UTF-8", newline="\n") as f:
        log_file = f.read()
        assert zero_division_err == log_file


def test_no_extension() -> None:
    @freeze_time("2025-05-08 04:00:00")
    @log("some_name")
    def some_func() -> str:
        return "Здесь могла бы быть ваша реклама"

    with pytest.raises(ValueError):
        some_func()
