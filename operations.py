def get_operator() -> bool | str:
    """
    Запрашивает у пользователя значение,
    проверяет и возвращает корректное значение-оператор либо False
    :return: "+", "-", "*", "/" or False
    """
    operator = input("Введите оператор +, -, *, /, %, ^: ")

    match operator:
        case "+" | "-" | "*" | "/" | "%" | "^":
            return operator
        case _:
            return False


def calc(num1, num2, operator) -> int | float:
    """
    Производит расчет и возвращает результат.

    :param num1: число 1
    :param num2: число 2
    :param operator: Оператор.
    :return: Результат вычисления.
    """
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case "^":
            return num1 ** num2

