"""
1. Необхідно створіти список випадкових чисел із випадковою кількістю елементів від 3 до 10.

2. Створить інший список з 3 елементів зі списку з п.1 - першим, третім і другим з кінця.
"""

import random
rands_num = random.randint(3, 10)
free_list = []

for i in range(rands_num):
    number = random.randint(1, 100)
    free_list.append(number)


first = free_list [0]
second = free_list [-1]
third = free_list [2]
pre_last = free_list [-2]

new_rand_list = [first,third, pre_last]
next_rand_list = [first,second, pre_last]

print("Список 1:", free_list )
print("Список 2:", new_rand_list)
print("Список 3:", next_rand_list)
