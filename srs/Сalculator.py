import re


def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
    else:
        return "Ошибка: неверный оператор"


while True:
    try:
        expr = input("Введите выражение (например, 5+3 или 4 * 2) или 'exit' для выхода: ").replace(" ", "")
        if expr.lower() == 'exit':
            break

        match = re.match(r"(-?\d+\.?\d*)([+\-*/])(-?\d+\.?\d*)", expr)
        if match:
            num1, operator, num2 = match.groups()
            num1, num2 = float(num1), float(num2)
            print("Результат:", calculate(num1, operator, num2))
        else:
            print("Ошибка: некорректный ввод")
    except ValueError:
        print("Ошибка: некорректный ввод")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
