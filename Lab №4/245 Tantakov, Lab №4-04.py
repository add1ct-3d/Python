print("Задание №4 \n")

n = int(input("Введите количество школьников: "))
k = int(input("Введите количество мандаринов: "))

mandarin_stud = k // n
remaining_stud = k % n

print(f"Каждому школьнику достанется: {mandarin_stud}")
print(f"В корзине останется: {remaining_stud}")

# input("Нажмите Enter, чтобы закрыть программу...")

