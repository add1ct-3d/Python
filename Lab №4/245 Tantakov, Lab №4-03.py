print("Задание №3 \n")

def split_number(x):
    thousands = x // 1000
    print(f"Цифра в позиции тысяч = {thousands}")
 
    hundreds = (x // 100)%10
    print(f"Цифра в позиции сотни = {hundreds}")

    tens = (x // 10) % 10
    print(f"Цифра в позиции десяток = {tens}")

    units = x % 10
    print(f"Цифра в позиции единиц = {units}")

try:
    x = int(input("Введите целое четырёхзначное число: "))

    if 1000 <= x <= 9999:
        split_number(x)

    else:
        print("Ошибка! Число должно быть четырёхзначным и положительным!")

except ValueError:
    print("Ошибка! Нужно ввести число!")

# input("Нажмите Enter, чтобы закрыть программу...")