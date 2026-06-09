print("Задание №2 \n"
      "\"Произведение\" \n")

product = 1

try:
    while True:
        positive_number = int(input("Введите число: "))

        if positive_number >= 0:
            product *= positive_number

        else:
            print("\nЦикл while остановлен. \n")
            break

    print(f"Результат произведения: {product}")
    
except ValueError:
    print("Ошибка! Используйте числа!")

# input("Нажмите Enter, чтобы закрыть программу...")