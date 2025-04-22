# Описание проекта
Домашняя работа по второму модулю обучения. Данный проект будет дорабатываться с каждым новым заданием.

---

## Установка
1. Клонирование репозитория
```
git clone https://github.com/ragveil/homework_bank_widget.git
```
2. Установка зависимостей
```
poetry install
```

## Основной функционал
Основной файл `main.py` служит для базовой проверки работы функций, а также содержит бонусный функционал для дополнительной проверки.

---
## Описание модуля `masks`
Модуль `masks` предоставляет функции:  
`get_mask_card_number` для маскировки номеров банковских карт;  
`get_mask_account` для маскировки номеров банковского счета.

### Примеры использования модуля `masks`
```python
from src.masks import get_mask_card_number, get_mask_account

# Маскировка номера карты
card_number = '7000792289606361'
masked_card = get_mask_card_number(card_number)
print(masked_card)  # Вывод: 7000 79** **** 6361

# Маскировка номера счета
account_number = '73654108430135874305'
masked_account = get_mask_account(account_number)
print(masked_account)  # Вывод: **4305
```
---
## Описание модуля `widget`
Модуль `widget` предоставляет функции:  
`mask_account_card` для маскировки номеров банковских карт и счетов в формате "Текст номер";  
`get_date` для форматирования даты в удобочитаемый формат.


### Примеры использования модуля `widget`
```python
from src.widget import mask_account_card, get_date

# Маскировка номера карты
card_number = "Visa Gold 5999414228426353"
masked_card = mask_account_card(card_number)
print(masked_card)  # Вывод: Visa Gold 5999 41** **** 6353

# Маскировка номера счета
account_number = "Счет 73654108430135874305"
masked_account = mask_account_card(card_number)
print(masked_account)  # Вывод: Счет **4305

# Форматирование даты
date_original = "2024-03-11T02:26:18.671407"
formatted_date = get_date(date_original)
print(formatted_date)  # Вывод: 11.03.2024
```
---
## Описание бонусной функции `bonus_generate_random`
Функция `bonus_generate_random` располагается в `main.py`, является результатом собственной инициативы и предназначена для тестирования работы модулей проекта.  

Функция:  
* генерирует номера карт формата различных международных платежных систем, таких как "Visa", "MasterCard", "Maestro" и прочие;  
* генерирует номера банковского счета;  
* возвращает скрытые маской значения.

### Примеры работы функции `bonus_generate_random`
```python
from src.main import bonus_generate_random

# Генерация и маскировка номера карты
user_input = 'card'
masked_card = bonus_generate_random(user_input)
print(masked_card)  # Вывод: МИР 8547 33** **** 8359

# Генерация и маскировка номера счета
user_input = 'account'
masked_account = bonus_generate_random(user_input)
print(masked_account)  # Вывод: Счет **2366
```
---
## Описание модуля `processing`
Модуль `processing` предоставляет функции:
`filter_by_state` для фильтрации банковских операций по состоянию;
`sort_by_date` для сортировки банковских операций по дате.

### Примеры использования модуля `processing`
```python
from src.processing import filter_by_state, sort_by_date

# Фильтрация банковских операций
banking_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]
filtered_operations = filter_by_state(banking_operations, state='CANCELED')
print(filtered_operations)  # Вывод: [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]

# Сортировка банковских операций по дате
banking_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]
sorted_operations = sort_by_date(banking_operations)
print(sorted_operations)  # Вывод: [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}] 
```
