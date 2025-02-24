def add(a: int | float, b: int | float) -> int | float:
    return a + b


def sub(a: int | float, b: int | float) -> int | float:
    return a - b


def multi(a: int | float, b: int | float) -> int | float:
    return a * b


def div(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise ZeroDivisionError("[Ошибка] Деление на ноль!")

    return a / b


def remainder(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise ZeroDivisionError("[Ошибка] Деление на ноль!")

    return a % b


def power(base: int | float, exp: int | float) -> int | float:
    return base ** exp
