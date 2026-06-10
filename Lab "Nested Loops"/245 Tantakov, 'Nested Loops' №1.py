print("Задание №1 \n"
"\"Шахматная доска\" \n")

for size in range(8):
    for sizev2 in range(8):
        if (size + sizev2) % 2 == 0:
            print("W", end=" ")
        else:
            print("B", end=" ")
    print()
