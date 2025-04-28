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
