
number = int(input("Введіть число: "))
while number > 9:
    nums = 1
    for digit in str(number):
        nums *= int(digit)
    number = nums

print(f"Результат: {number}")