import string

letters_range = input("Введіть діапазон (напр. a-f): ")


start_char = letters_range.split('-')
end_char = letters_range.split('-')


alphabet = string.ascii_letters
start_index = alphabet.find(start_char)
end_index = alphabet.find(end_char)

print(alphabet[alphabet.index(start_char) : alphabet.index(end_char) + 1])