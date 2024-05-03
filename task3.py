def prime_in_range(num1, num2):
    prime_nums_in_range = []
    for i in range(num1, num2+1):
        if i == 2:
            prime_nums_in_range.append(i)
        if i%2 == 0:
            continue
        for t in range(3, i): # мы всегда можем поделить на 1, деление на 2 проверяется, начинаем с 3
            if i%t == 0:
                break
            if i not in prime_nums_in_range:
                prime_nums_in_range.append(i)
    return prime_nums_in_range

print(prime_in_range(11, 20)) # [11, 13, 17, 19]
print(prime_in_range(2, 23)) # [2, 5, 7, 11, 13, 17, 19, 23]