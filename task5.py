a = int(input())
b = int(input())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("No")
else:
    x = -b // a  # Используем оператор целочисленного деления //
    print("x =", x)
