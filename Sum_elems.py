
numbers = [ 2, 3, 4, 5]


if not numbers:
    result = 0
else:
    result = sum(numbers[::2]) * numbers[-1]

print(result)

number2 =[0,1,7,2,4,8]

if not number2:
    result = 0
else:
    result = sum(number2[::2]) * number2[-1]

print(result)