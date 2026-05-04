print("Задача №5 \"Расчёт премии\" \n")

oklad = int(input("Введите оклад сотрудника: "))

try:
    if oklad > 5000:
        premia = oklad * 0.10

    else:
        premia = oklad * 0.12

    print (f"Премия сотрудника = {premia} рублей")

except ValueError:
    print ("Ошибка! Введите целое число!")

input("Нажмите Enter, чтобы закрыть программу...")