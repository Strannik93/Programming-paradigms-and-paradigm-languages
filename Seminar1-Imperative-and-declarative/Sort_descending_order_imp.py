def sort_list_imperative(numbers):
    if len(numbers) <= 1:
        return numbers
    check = True
    current_i = 0
    while check == True:
        check = False
        for i in range(len(numbers) - 1 - current_i):
            if numbers[i] < numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                check = True
        current_i += 1
    return numbers


numbers = [2,6,8,3,5,1,9,4]
print(numbers)
print(sort_list_imperative(numbers))