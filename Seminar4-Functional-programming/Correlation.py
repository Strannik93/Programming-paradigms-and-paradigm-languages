import numpy as np

# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).

# Создаем массив из 20 случайных значении в диапозоне от 0 до 15
massiv_1 = np.random.randint(0,15,20)
print(massiv_1)

# Создаем положительно коррелированный массив с некоторым случайным шумом
massiv_2 = massiv_1 + np.random.normal(0,15,20)
print(massiv_2)

# Рассчитывем корреляцию между массивами
rxy = np.corrcoef(massiv_1,massiv_2)
print(rxy)