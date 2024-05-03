from collections import Counter

def check_arr(arr):  
    common_dividers = []
    dividers = []
    for num in arr:
        for i in range(1, num+1):
            if num%i == 0:
                dividers.append(i)
    count_dividers = Counter(dividers)
    for i in dividers:
        if count_dividers[i] == len(arr) and i != 1: 
            # По примеру из условия, единица не учитывается, если стереть and i != 1, то на выходе всегда будет выводиться и она как общий делитель
            if i in common_dividers:
                continue
            common_dividers.append(i)
    return common_dividers

print(check_arr([54, 94, 106])) # [2]
print(check_arr([42, 12, 18])) # [2, 3, 6]

