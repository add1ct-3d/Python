print("Задание №1 \n"
      "\"Пароль\" \n")

max_attempts = 3
attempts = 0

correct_password = "admin"

while True:
    password = (str(input("Введите пароль (буквами): ")))

    if password == correct_password:
        print("Доступ разрешён. Вы вошли в систему. \n")
        break

    else:
        attempts += 1
        print(f"Неверный пароль. Осталось попыток: {max_attempts - attempts} \n")

        if attempts >= max_attempts:
            print("Доступ запрещен. Пожалуйста, повторите попытку позже. \n")
            break

# input("Нажмите Enter, чтобы закрыть программу...")