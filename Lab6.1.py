db_input = input("Введите последовательность чисел, разделенных пробелом: ")
num_list = list(map(int, db_input.split()))
nums_tuple = tuple(num_list)
print("Список чисел:", num_list)
print("Кортеж чисел:", nums_tuple)