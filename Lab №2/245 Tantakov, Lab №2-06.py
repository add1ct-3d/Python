print("Задача №6 \n")

two_digit_numb = int(input("Введите двузначное число: "))

if two_digit_numb < 10 or two_digit_numb > 99:
    print("Ошибка! Число должно быть двухзначным (от 10 до 99).")

else:
    tens = two_digit_numb // 10
    units = two_digit_numb % 10

print(f"Число: {two_digit_numb}")
print(f"Десятки: {tens}")
print(f"Единицы: {units}")

input("Нажмите Enter, чтобы закрыть программу...")