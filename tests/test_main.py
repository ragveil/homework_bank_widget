import random

import pytest

from src.main import bonus_generate_random


@pytest.mark.parametrize(
    "keyword, expected",
    [
        ("card", "Visa 9310 70** **** 4343"),
        ("CARD", "Visa 9310 70** **** 4343"),
        ("account", "Счет **1480"),
        ("ACCOUNT", "Счет **1480"),
        ("", "Некорректные данные"),
        (" ", "Некорректные данные"),
        ("Карта", "Некорректные данные"),
    ],
)
def test_bonus_generate_random_both(keyword: str, expected: str) -> None:
    """
    Тестируем бонусную функцию bonus_generate_random с использованием различных входных данных.
    В данном тесте используется параметризация.
    :param keyword: Входные данные в виде строки.
    :param expected: Ожидаемый результат.
    :return: Результат работы теста.
    """
    random.seed(88)
    assert bonus_generate_random(keyword) == expected
