# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def search(value: int, search_list: list, min = 0, max = None):
    if max == None: max = len(search_list) - 1
    if max < min: return -1
    mid_point = (max - min)//2 + min
    if search_list[mid_point] < value: return search(value, search_list, mid_point+1, max)
    elif search_list[mid_point] > value: return search(value, search_list, min, mid_point-1)
    else: return mid_point

my_list = [1,3,4,6,7,8,10,13,14]
find_value = 4
print(my_list)
find_index = search(find_value,my_list)
if find_index == -1:
    print(f"Искомое число {find_value} не найдено")
else:
    print(f"Искомое число {find_value} с индексом {find_index}")