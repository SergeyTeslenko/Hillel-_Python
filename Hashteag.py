import string

text = input("Введіть текст: ")


for char in string.punctuation:
    text = text.replace(char, ' ')


hashtag = '#' + ''.join(word.capitalize() for word in text.split())


hashtag = hashtag[:140]

print(hashtag)