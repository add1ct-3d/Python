import math

print("Задание №4 \n" \
"Калькулятор площади круга и прямоугольника \n")

width, height = map(float, input("Введите ширину и высоту прямоугольника (через пробел): ").split())

def calculate_rectangle_area(width, height):
    """Возваращает площадь прямоугольника"""
    return width * height

rectangle_area = calculate_rectangle_area(width, height)

print(f"Площадь прямоугольника: {rectangle_area} \n")

radius = float(input("Введите радиус круга: "))

def calculate_circle_area(radius):
    """Возвращает площадь круга"""
    return math.pi * radius**2

circle_area = calculate_circle_area(radius)

print(f"Площадь круга: {circle_area:.1f} \n")

# help(calculate_rectangle_area)
# help(calculate_circle_area)

# # input("Нажмите Enter, чтобы закрыть программу...")
