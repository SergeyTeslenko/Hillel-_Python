import string

user_info = input("Введіть через дефіс дві літери: ").strip()

if len(user_info ) >= 2 and ((user_info [0] == user_info [-1]) and user_info [0] in "\"'"):
    user_info = user_info [1:-1]

left_part, right_part = user_info .split('-', 1)
left = left_part.strip()[0]
right = right_part.strip()[0]

letters = string.ascii_letters
#print(letters)
start = letters.index(left)
end = letters.index(right)

print(letters[start:end + 1])