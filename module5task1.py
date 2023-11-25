'''Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів:
 [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

    'Alex\nKdfe23\t\f\v.\r'
    'Al\nKdfe23\t\v.\r'
'''
def real_len(text: str):
    replace_symbols = ['\n', '\f', '\r', '\t', '\v']
    for symbol in replace_symbols:
        text = text.replace(symbol, '')
    return len(text)

print(real_len('AlexKdfe23.'))
print(real_len('AlKdfe23.'))