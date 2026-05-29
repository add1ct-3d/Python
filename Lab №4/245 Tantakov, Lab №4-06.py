import math

print("Задание №4 \n" \
"sin(x) + cos(x) + tan(x)^2 \n")

try:
    x = float(input("Введите значение числа x: "))
    rad_x = math.radians(x)
    summa = math.sin(rad_x) + math.cos(rad_x) + math.tan(rad_x)**2
    print(f"Ответ: {summa}")
except ValueError:
    print("Ошибка! Введите число!")

# input("Нажмите Enter, чтобы закрыть программу...")
