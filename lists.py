list = [1, 2, 3, 4, 5,6,7,8,9,10]

mid_list = (len(list) + 1) // 2
result = [list[:mid_list], list[mid_list:]]

print(result)