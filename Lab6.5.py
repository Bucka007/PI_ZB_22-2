students = [("Alice", 22, 4.5), ("Bob", 20, 3.8), ("Charlie", 21, 4.9), ("Diana", 23, 4.2)]

def best_student(students_list):
    best = students_list[0]
    for student in students_list:
        if student[2] > best[2]:
            best = student
    return best

test1 = best_student(students)
print("Лучший студент:", test1[0])

students.append(("Eve", 24, 4.7))
test2 = best_student(students)
print("Лучший студент после добавления Еve:", test2[0])

students.remove(test2)
test3 = best_student(students)
print("Лучший студент после удаления лучшего:", test3[0])
