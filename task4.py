num = int(input())
roman = ''
while num > 0:
    if num >= 100:
        roman += 'C'
        num -= 100
    elif num >= 90:
        roman += 'XC'
        num -= 90
    elif num >= 50:
        roman += 'L'
        num -= 50
    elif num >= 40:
        roman += 'XL'
        num -= 40
    elif num >= 10:
        roman += 'X'
        num -= 10
    elif num >= 9:
        roman += 'IX'
        num -= 9
    elif num >= 5:
        roman += 'V'
        num -= 5
    elif num >= 4:
        roman += 'IV'
        num -= 4
    else:
        roman += 'I'
        num -= 1
print(roman)