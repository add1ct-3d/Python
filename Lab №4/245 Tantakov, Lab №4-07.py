print("Задание №7 \n")

places_in_compartment = 4

try: 
    seat_number = int(input("Введите номер места: "))

    if seat_number < 1  or seat_number > 36: # по условию задачи всего 9 купе = 36 мест
        print("Такого места нет!")
    else:
        cupe = (seat_number - 1) // places_in_compartment + 1
        print(f"Номер купе: {cupe}")

except ValueError:
    print("Ошибка! Введите целое число (номер места)!")

# input("Нажмите Enter, чтобы закрыть программу...")