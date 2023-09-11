# Задача-2: У вас есть массив, содержащий числа от 1 до N, где N - длина массива.
# Одно из чисел в массиве повторяется дважды, а одно число пропущено.
# Найдите повторяющееся число и пропущенное число.

massiv = [2, 3, 1, 5, 3]

print(massiv)

repeating_number = None
missed_number = None
n = len(massiv)

current = 1
while (repeating_number == None or missed_number == None) and current <= n:
    count = 0
    for item in massiv:
        if item == current:
            count += 1
            if count == 2:
                repeating_number = current
                break
    if count == 0:
        missed_number = current
    current += 1

print("Повторяющееся число:")
print(repeating_number)
print("Пропущенное число:")
print(missed_number)