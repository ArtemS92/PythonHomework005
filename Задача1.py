# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('text.txt', 'r', encoding='utf-8') as text:  # входной текст в файле text.txt
    text = text.read().split()
    print(text)

text2 = list(filter(lambda i: 'абв' not in i, text))

with open('new_text.txt', 'w', encoding='utf-8') as new_text:
    new_text = new_text.write(f'{text2}')

with open('new_text.txt', 'r', encoding='utf-8') as new_text:
    new_text = new_text.read()
    print(new_text)
