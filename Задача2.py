# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('rle.txt', 'r', encoding='utf -8') as rle:
    rle = rle.read()
    print(rle)


def encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        encoding += str(count) + s[i]
        i = i + 1

    return encoding


print(encode(rle))

with open('final_rle.txt', 'w', encoding='utf-8') as final_rle:
    final_rle = final_rle.write(f'{encode(rle)}')
