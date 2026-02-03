name = input("Користувач будь ласка введіть рядок: ")


res = not name[0].isdigit()

if any(char.isupper() for char in name):
    res = False


punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~ '
for char in name:
    if char in punctuation:
        res = False


if name.count("_") > 1:
    res = False


not_exist = ["if", "else", "while", "for", "return", "def", "class", "pass"]
if name in not_exist:
    res = False

print(res)