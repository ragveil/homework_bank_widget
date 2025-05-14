import time
from functools import wraps
from typing import Any, Callable, Generator, Literal

from src.constants import PATH_TO_LOGS


def log(filename: Literal[False] | str = False) -> Callable[[Any], Any]:
    """
    Функция-декоратор для ведения логов. Записывает лог в файл, если задано имя файла, и в консоль - если нет.
    :param filename: Необязательный параметр, имя файла в виде строки.
    :return: Результат работы функции.
    """

    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            decl_pos = "позиционный" if len(args) == 1 else "позиционных"
            decl_named = "именованный" if len(kwargs) == 1 else "именованных"
            try:
                start_timestamp = time.time()
                start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                result = func(*args, **kwargs)
                end_timestamp = time.time()
                end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                log_message = (
                    f"Начало выполнения функции: {start}\n"
                    f"Выполняемая функция: {func.__name__}\n"
                    f"Переданные аргументы:\n"
                    f"{len(args)} {decl_pos} {'' if len(args) == 0 else str(args)}\n"
                    f"{len(kwargs)} {decl_named} {'' if len(kwargs) == 0 else str(kwargs)}\n"
                    f"Окончание работы функции: {end}\n"
                    f"Результат работы функции: {next(result) if isinstance(result, Generator) else result}\n"
                    f"Время работы функции: {round(((end_timestamp - start_timestamp) * 1000), 5)}ms."
                )
                if filename is False:
                    print(log_message)
                elif ".txt" in filename:
                    with open(PATH_TO_LOGS + filename, "w", encoding="UTF-8", newline="\n") as f:
                        f.write(log_message)
                        f.write("\n")
                else:
                    raise ValueError("Задано неверное расширение файла")
                return result

            except Exception as e:
                log_message = (
                    f"Время возникновения ошибки: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}\n"
                    f"Сбой функции {func.__name__}. Ошибка {type(e).__name__}\n"
                    f"Переданные аргументы:\n"
                    f"{len(args)} {decl_pos} {'' if len(args) == 0 else str(args)}\n"
                    f"{len(kwargs)} {decl_named} {'' if len(kwargs) == 0 else str(kwargs)}\n"
                )
                if filename is False:
                    print(log_message)
                elif ".txt" in filename:
                    with open(PATH_TO_LOGS + filename, "w", encoding="UTF-8", newline="\n") as f:
                        f.write(log_message)
                        f.write("\n")
                else:
                    raise ValueError("Задано неверное расширение файла")

        return wrapper

    return decorator
