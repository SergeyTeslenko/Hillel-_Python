def popular_words(text, words):

    lower_text= text.lower().split()

    return {word: lower_text.count(word) for word in words}


result = popular_words('''
When I was One I had just begun
When I was Two I was nearly new
''', ['i', 'was', 'three', 'near'])

print(result)