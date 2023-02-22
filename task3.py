rides = int(input())
arr = [0, 0, 0]
while(rides>0):
    if((rides//60)<(rides//10)):
        rides -= 60
        arr[2] += 1
    elif((rides//10)<(rides//1)):
        rides -= 10
        arr[1] += 1
    else:
        rides -= 1
        arr[0] += 1

print(arr)