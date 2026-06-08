print("Задание №1 \nКалькулятор налогов \n"
      "Налоговая ставка: 13% \n")

income_tax = float(input("Введите свой годовой доход: "))

TAX_RATE = 0.13     # Константа для налоговой ставки 13%

calculated_tax = income_tax * TAX_RATE      # Рассчитаный налог

net_income = income_tax - calculated_tax      # Общая сумма после вычета налога

# Отформатированные строки
income_str = f"{income_tax:,.2f}".replace(",", " ")
tax_str = f"{calculated_tax:,.2f}".replace(",", " ")
net_str = f"{net_income:,.2f}".replace(",", " ")

print(
    f"Общая сумма дохода: {income_str} руб.\n"
    f"Сумма рассчитанного налога: {tax_str} руб.\n"
    f"Сумма «на руки» после вычета налога: {net_str} руб."
)

# input("Нажмите Enter, чтобы закрыть программу...")
