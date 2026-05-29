import math

print("Задание №2")

def input_point(name):
    print(f"Введите координаты точки {name}: ")
    x = float(input("x = "))
    y = float(input("y = "))
    print()
    return(x, y)

point_1 = input_point("1")
point_2 = input_point("2")

print(f"Данные точки 1: {point_1}")
print(f"Данные точки 2: {point_2} \n")

euclid_dist = math.sqrt(    (point_1[0] - point_2[0])**2    +  (point_1[1] - point_2[1])**2    )
print(f"Евклидово расстояние между двумя точками = {euclid_dist}")

# input("Нажмите Enter, чтобы закрыть программу...")