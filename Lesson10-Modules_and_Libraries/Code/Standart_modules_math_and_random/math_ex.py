import math


# 1. Найти длину окружности с определенным радиусом:
r = 100
print(f'1. Найти длину окружности с радиусом {r}:\t'
      f'{2 * math.pi * r}')

# 2. Найти площадь окружности с определенным радиусом:
print(f'2. Найти площадь окружности с радиусом {r}:\t'
      f'{math.pi * math.pow(r, 2)}')

# 3. По координатам 2-х точек определить расстояние между ними:
x1, y1 = 10, 10
x2, y2 = 50, 100
length = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
print('3. Определить расстояние между точками:\n'
      f'1) A({x1}, {y1});\n'
      f'2) B({x2}, {y2}).\n'
      f'Расстояние от A до B -> {length}')

# 4. Найти факториал числа 9:
print('4. Найти факториал числа 9:\n'
      f'9! = {math.factorial(9)}')
