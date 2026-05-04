print("Задача №4 \n")

day = 1
distance = 10

while distance <= 20:
    print(f"День {day}: {distance} км")

    day += 1
    distance *= 1.1

print(f"\nЛыжник впервые пробежал больше 20 км на {day} день")
print(f"День {day}: {distance} км \n")

input("Нажмите Enter, чтобы закрыть программу...")