print('Введите число')

input_num = input()

def check_num(input_num):
    declension = ['', 'а', 'ов']

    word = 'компьютер'

    strip_num = input_num[-2:]

    if len(strip_num) == 2 and strip_num in '11 12 13 14 15 16 17 18 19':
        return f'{input_num} {word}{declension[2]}'
    elif strip_num[-1] in '234':
        return f'{input_num} {word}{declension[1]}'
    elif strip_num[-1] in '56789':
        return f'{input_num} {word}{declension[2]}'
    else:
        return f'{input_num} {word}{declension[0]}'
    
print(check_num(input_num))
