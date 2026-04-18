print("Вы запустили простой калькулятор! \n")

numb1 = float(input("Введите первое число: "))
numb2 = float(input("Введите второе число: "))
operation = input("Выберите математическую операцию (+, -, *, /): ")

match operation:
    case "+":
        result = numb1 + numb2
    
    case "-":
        result = numb1 - numb2
    
    case "*":
        result = numb1 * numb2

    case "/":
        if numb2 == 0:
            result = "Ошибка: деление на ноль невозможно!"

        else:
            result = numb1 / numb2

    case _:
        result = "Ошибка! Неизвестная операция (выберите нужную)."

if result == "Ошибка: деление на ноль невозможно!" or result == "Ошибка! Неизвестная операция (выберите нужную).":
    print(f"{result}\n")

else:
    print(f"{numb1} {operation} {numb2} = {result}\n")

input("Нажмите Enter, чтобы закрыть программу...")



