import sys

# Зчитування розмірів паралелепіпеда з аргументів командного рядка
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

# Обчислення об'єму та площі поверхні
volume = a * b * c
surface_area = 2 * (a * b + b * c + a * c)

# Виведення результатів
print(f"Об'єм паралелепіпеда: {volume}")
print(f"Площа поверхні: {surface_area}")