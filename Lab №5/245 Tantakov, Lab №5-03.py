print("Задание №3 \n" \
"Конвертер доллара США к российскому рублю (курс 72,97₽)\n")

dolar_amount = float(input("Введите сумму в долларах: "))

def convert_to_rub(amount_usd):
    """
    Функция convert_to_rub переводит сумму из долларов в рубли.

    Принимает:
    amount_usd (float) — сумма в долларах

    Возвращает:
    float — сумма в рублях по курсу 72.97
    
    """
    USD_TO_RUB = 72.97       # Отдельная переменная для курса доллара к рублю
    result = amount_usd * USD_TO_RUB
    return result

rub_amount = convert_to_rub(dolar_amount)

print(f"Сумма в рублях: {rub_amount} \n")

# help(convert_to_rub)

# # input("Нажмите Enter, чтобы закрыть программу...")