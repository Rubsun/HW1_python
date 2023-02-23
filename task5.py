a, b = int(input()), int(input())

if a != b: #корень есть только тогда, когда а != в.
    if b % a == 0: #Проверка на существование целого корня
        print(-b // a) #Вычесление корня

    else:
        print('NO')

    if b == 0:
        print('INF')
else:
    print('NO')
