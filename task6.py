a,b,c = int(input()), int(input()), int(input())
D = (b ** 2) - (4 * a * c) #Нахожу дискрименант
if a != 0:
    if D > 0: #Вычесление корней уравнения исходя из значения D
        x1 = (-b + D ** 0.5) // 2 * a
        x2 = (-b - D ** 0.5) // 2 * a
        print(x1, x2)
    elif D == 0:
        x1 = (-b + D ** 0.5) // 2 * a
    else:
        print()
