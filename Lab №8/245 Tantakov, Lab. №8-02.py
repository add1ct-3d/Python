print("Задание №2 \n")

try:
    for i in range(1, 10+1):
        number = int(input(f"Введите {i}-ое число: "))

except ValueError:
    print("Ошибка! Введите целое число!")