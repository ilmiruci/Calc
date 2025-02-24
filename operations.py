def addition(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2

def sub(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2

def multi(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2

def div(num1: int | float, num2: int | float) -> int | float:
    if num2 == 0:
        raise ZeroDivisionError("[Ошибка] Деление на ноль!")

    return num1 / num2

def remainder(num1: int | float, num2: int | float) -> int | float:
    if num2 == 0:
        raise ZeroDivisionError("[Ошибка] Деление на ноль!")

    return num1 % num2

def power(base: int | float, exp: int | float) -> int | float:
    return base ** exp

