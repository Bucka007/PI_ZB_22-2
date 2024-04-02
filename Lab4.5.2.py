from Lab4_5_1 import calc_treug
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

treug = calc_treug(a, b, c)
print(f"Площадь треугольника: {treug}")