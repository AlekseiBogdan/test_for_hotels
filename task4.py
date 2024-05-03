def multiply_table(num):
    numbers = []
    for i in range(1, num+1):
        number_muliply_list = []
        for t in range(1, num+1):
            mulitply = i*t
            number_muliply_list.append(mulitply)
        numbers.append(number_muliply_list)
    rows_output = ' '.join(str(i) for i in range(1, num+1)) + '\n'
    for i in numbers[0]:
        row = str(i) + ' '
        for t in numbers:
            row += str(t[numbers[0].index(i)])
            row += ' '
        row += '\n'
        rows_output += row
    print(' ', rows_output)

multiply_table(5)