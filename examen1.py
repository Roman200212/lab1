def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Треугольника не существует"
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "Треугольник существует"
    else:
        return "Треугольника не существует" # В остальных случаях, треугольника не существует
