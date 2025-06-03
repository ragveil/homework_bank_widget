from src.advanced_func import count_categories, search_item


def test_search_items(json_sample: list[dict[str, str | int]], maestro: list[dict[str, str | int]]) -> None:
    assert search_item(json_sample, keyword="перевод") == json_sample
    assert search_item(json_sample, keyword="слово") == json_sample
    assert search_item(json_sample, keyword="Maestro") == maestro


def test_count_categories(json_sample: list[dict[str, str | int]], categories: list[str]) -> None:
    assert count_categories(json_sample, categories) == {"Перевод организации": 3}
    assert count_categories(json_sample, []) == {}
