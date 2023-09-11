# Задача- 1: У вас есть массив целых чисел, в котором каждое число, кроме одного, повторяется дважды.
# Вам нужно найти это одиночное число.

massiv = [4, 3, 1, 4, 1, 3, 2]

print(massiv)

check = True
current = 1
while check and current <= len(massiv)/2 + 1:
    count = 0
    for item in massiv:
        if item == current:
            count += 1
            if count == 2:
                break
    if count == 1:
        check = False
    else: current += 1

print("Одиночное число: ")
print(current)