import operations


def calc():
    print("Программа калькулятор\n"
          "Введите два числа, операцию и получите результат")

    operators: str = "+-*/%^"
    operator: str = input(f"Введите оператор {", ".join(operators)}: ")

    if operator not in operators:
        print("[Ошибка] Недоступная операция...")

    try:
        user_num1 = float(input("Введите первое число: "))
        user_num2 = float(input("Введите второе число: "))

        match operator:
            case "+":
                print(operations.addition(user_num1, user_num2))
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

    except ZeroDivisionError as err:
        print(err)
    except ValueError:
        print("Вы ввели неправильное значение")


if __name__ == "__main__":
    calc()
