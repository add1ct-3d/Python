print("Задание №7 \n")

count = 0

try:
    for i in range(1, 30+1):
        power = int(input(f"Введите мощность {i}-ой машины: "))

        if power > 200:
            count += 1

    print(f"Количество моделей, мощность двигателя которых > 200 единиц силы: {count} \n")

except ValueError:
    print("Ошибка! Введите целые значения! \n")

input("Нажмите Enter, чтобы закрыть программу...")