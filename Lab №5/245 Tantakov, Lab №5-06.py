import math

def calculate_distance(x1, y1, x2, y2):
    """Возвращает расстояние между двумя точками (x1, y1) и (x2, y2)"""
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # Формула расстояния между двумя точками на плоскости
    return distance

def calculate_triangle_area(a, b, c):
    """Возвращает площадь треугольника со сторонами a, b, c по формуле Герона"""
    p = (a + b + c) / 2
    square = math.sqrt(p * (p - a) * (p - b) * (p - c)) # Формула Герона
    return square

x_a = int(input("Введите x координату точки A: "))
y_a = int(input("Введите y координату точки A: "))
print()

x_b = int(input("Введите x координату точки B: "))
y_b = int(input("Введите y координату точки B: "))
print()

x_c = int(input("Введите x координату точки C: "))
y_c = int(input("Введите y координату точки C: "))
print()

# Вызываем calculate_distance 3 раза, передавая координаты каждой пары точек
AB = calculate_distance(x_a, y_a, x_b, y_b)
BC = calculate_distance(x_b, y_b, x_c, y_c)
AC = calculate_distance(x_a, y_a, x_c, y_c)

# Передаём длины сторон в calculate_triangle_area, получаем площадь по формуле Герона
triangle_area = calculate_triangle_area(AB, BC, AC)

print(f"Площадь треугольника (по формуле Герона): {triangle_area:.2f}") # Форматирование до 2-х знаков после запятой

# help(calculate_distance)
# help(calculate_triangle_area)

# # input("Нажмите Enter, чтобы закрыть программу...")

    