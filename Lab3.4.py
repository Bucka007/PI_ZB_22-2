a = input("Введите предложение на английском: ")

print("Длина предложения:", len(a))

print("Предложение в нижнем регистре:", a.lower())

print("Количество гласных в предложении:", sum(1 for char in a.lower() if char in 'aeiou'))

print("Предложение с заменой 'ugly' на 'beauty':", a.lower().replace("ugly", "beauty"))

print("Предложение начинается с 'The':", a.lower().startswith("the"))
print("Предложение заканчивается на 'end':", a.lower().endswith("end"))