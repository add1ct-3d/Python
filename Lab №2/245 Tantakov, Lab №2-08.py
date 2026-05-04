print("Задача №8 \n")

day = 1
distance = 10   #пробег за один день
total = 0    # суммарный пробег

while total <= 100:
    total += distance
    print(f"День {day}: {distance} км  (сумма = {total} км)")

    if total > 100:
        break

    day += 1
    distance *= 1.1

print(f"\nСуммарный пробег превысил 100 км на {day} день")
print(f"Всего за {day} дней: {total} км \n")

input("Нажмите Enter, чтобы закрыть программу...")