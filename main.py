import operations


def calc():
    print("Программа калькулятор\n"
          "Введите два числа, операцию и получите результат")

    try:
        operator = operations.get_operator()
        user_num1 = int(input("Введите первое число: "))
        user_num2 = int(input("Введите второе число: "))

        if operator:  # Если значение True, то выполняем код
            result = operations.calc(user_num1, user_num2, operator)
            print(result)
        else:
            print("Такой оператор не предусмотрен")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except ValueError:
        print("Вы ввели неправильное значение")


if __name__ == "__main__":
    calc()
