import string

s = input().strip()
# видаляємо зовнішні лапки, якщо користувач ввів "a-c" або 'a-c'
if len(s) >= 2 and ((s[0] == s[-1]) and s[0] in "\"'"):
    s = s[1:-1]

left_part, right_part = s.split('-', 1)
left = left_part.strip()[0]
right = right_part.strip()[0]

letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
start = letters.index(left)
end = letters.index(right)

print(letters[start:end + 1])