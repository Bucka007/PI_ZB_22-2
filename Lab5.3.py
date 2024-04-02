one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

one_min, one_max = min(one), max(one)
two_min, two_max = min(two), max(two)
three_min, three_max = min(three), max(three)

one_treug_max = (one_max ** 2 - (one_max - one_min) ** 2) ** 0.5 / 2
one_treug_min = (one_min ** 2 - (one_min - one_max) ** 2) ** 0.5 / 2

two_treug_max = (two_max ** 2 - (two_max - two_min) ** 2) ** 0.5 / 2
two_treug_min = (two_min ** 2 - (two_min - two_max) ** 2) ** 0.5 / 2

three_treug_max = (three_max ** 2 - (three_max - three_min) ** 2) ** 0.5 / 2
three_treug_min = (three_min ** 2 - (three_min - three_max) ** 2) ** 0.5 / 2

print("Площадь треугольника из максимальных значений списка one:", one_treug_max)
print("Площадь треугольника из минимальных значений списка one:", one_treug_min)
print("Площадь треугольника из максимальных значений списка two:", two_treug_max)
print("Площадь треугольника из минимальных значений списка two:", two_treug_min)
print("Площадь треугольника из максимальных значений списка three:", three_treug_max)
print("Площадь треугольника из минимальных значений списка three:", three_treug_min)