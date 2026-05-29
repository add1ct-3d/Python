minutes = int(input("Введите количество минут: "))

hours = minutes // 60
remaining_minutes = minutes % 60

if hours == 1:
    word = "час"
elif hours >= 2 and hours <= 4:
    word = "часа"
else:
    word = "часов"

print(f"{minutes} минут это - {hours} {word} {remaining_minutes} минут")


# input("Нажмите Enter, чтобы закрыть программу...")
