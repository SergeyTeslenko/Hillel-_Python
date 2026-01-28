numbers_list = [1, 2, 3, 4, 5]

if len(numbers_list) > 1:
    last_element = numbers_list.pop()
    numbers_list.insert(0, last_element)

print(numbers_list)