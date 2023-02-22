arr = []
for i in range(3):
    arr.append(int(input()))
temp = 0
while(arr[2]>0): #Пока котлет > 1
    arr[2] -= arr[0] #Кладем максимальное кол-во котлет на сковороду
    temp = temp + arr[1]*2 #Вычесляем время жарки

print(temp)
