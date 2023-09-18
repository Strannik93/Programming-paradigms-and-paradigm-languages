# Есть список студентов с их именами и оценками.
# Нам нужно найти средний балл по всем студентам и вывести имена студентов, чей балл выше среднего.
# Структурный стиль.

# Список студентов
student_data = [
{'name': 'Alice', 'score': 85},
{'name': 'Bob', 'score': 92},
{'name': 'Charlie', 'score': 78},
{'name': 'David', 'score': 95},
]

# поиск среднего значения среди всех оценок
summ = 0
for student in student_data:
    summ += student['score']
average = summ/len(student_data)

# добавление подходящих студентов через сравнение оценок
above_average_students = []
for student in student_data:
    if student['score'] > average:
        above_average_students.append(student)

# Вывод среднего балла и студентов с баллом выше среднего
print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")