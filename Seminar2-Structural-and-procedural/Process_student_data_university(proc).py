# Есть список студентов с их именами и оценками.
# Нам нужно найти средний балл по всем студентам и вывести имена студентов, чей балл выше среднего.
# Процедурный стиль

# процедура для поиска среднего значения среди всех оценок
# принимает список студентов с полем 'score'
def find_average(students: list):
    summ = 0
    for student in students:
        summ += student['score']
    return summ/len(students)

# процедура для составления списка подходящих студентов через сравнение оценок
# принимает среднюю оценку для сравнения и список студентов с полем 'score'
def list_above_average(average: int, students: list):
    above_average_students = []
    for student in students:
        if student['score'] > average:
            above_average_students.append(student)
    return above_average_students

# Список студентов
student_data = [
{'name': 'Alice', 'score': 85},
{'name': 'Bob', 'score': 92},
{'name': 'Charlie', 'score': 78},
{'name': 'David', 'score': 95},
]

average = find_average(student_data)
above_average_students = list_above_average(average, student_data)

# Вывод среднего балла и студентов с баллом выше среднего
print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")