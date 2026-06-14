print("Задание №5 \n" \
"Банкомат \n")

amount_of_money = int(input("Введите сумму для снятия: "))

B5000 = amount_of_money // 5000
amount_of_money %= 5000

B2000 = amount_of_money // 2000
amount_of_money %= 2000

B1000 = amount_of_money // 1000
amount_of_money %= 1000

B500 = amount_of_money // 500
amount_of_money %= 500

B200 = amount_of_money // 200
amount_of_money %= 200

B100 = amount_of_money // 100

print(f"5000: {B5000}")
print(f"2000: {B2000}")
print(f"1000: {B1000}")
print(f"500: {B500}")
print(f"200: {B200}")
print(f"100: {B100}")