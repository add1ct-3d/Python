print("Вы запустили программу определение сезона!\n")

month = int(input("Введите номер месяца (от 1 до 12): "))

def month_info(month_number, season, season_emoji):
    print(f"Номер месяца: {month_number}")
    print(f"Введённый месяц: {season}")
    print(f"Соответствующий emoji: {season_emoji}\n")

match month:
    case 12 | 1 | 2:
        month_info(month, "Зима", "❄️")

    case 3 | 4 | 5:
        month_info(month, "Весна", "🌸")

    case 6 | 7 | 8:
        month_info(month, "Лето", "☀️")

    case 9 | 10 | 11:
        month_info(month, "Осень", "🍂")

    case _:
        print("Вы ввели неверный номер месяца! Пожалуйста, введите число от 1 до 12.\n")

input("Нажмите Enter, чтобы закрыть программу...")


