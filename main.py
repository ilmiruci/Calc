import operations


def calc() -> None:
    print("Программа калькулятор")
    print("Введите два числа, операцию и получите результат")

    operators: str = "+-*/%^"
    operator: str = input(f"Введите оператор: {', '.join(operators)}: ")

    if operator not in operators:
        print("[Ошибка] Недоступная операция...")
        return

    try:
        user_num1 = float(input("Введите первое число: "))
        user_num2 = float(input("Введите второе число: "))

        match operator:
            case "+":
                print(operations.add(user_num1, user_num2))
            case "-":
                print(operations.sub(user_num1, user_num2))
            case "*":
                print(operations.multi(user_num1, user_num2))
            case "/":
                print(operations.div(user_num1, user_num2))
            case "%":
                print(operations.remainder(user_num1, user_num2))
            case "^":
                print(operations.power(user_num1, user_num2))

    except ValueError:
        print("Вы ввели неправильное значение")
    except ZeroDivisionError as err:
        print(err)


if __name__ == "__main__":
    calc()
