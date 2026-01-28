my_numbers = [1, 2, 3, 4, 5, 6]
sliced_list = (len(my_numbers) + 1) // 2
result = [my_numbers[:sliced_list], my_numbers[sliced_list:]]
print(result)