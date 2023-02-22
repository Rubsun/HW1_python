arr = []
isEquals = False
for i in range(4):
    arr.append(int(input()))

if (arr[0]>0 and arr[2]>0) and (arr[1]>0 and arr[3]>0):
    isEquals = True

elif (arr[0]<0 and arr[2]<0) and (arr[1]<0 and arr[3]<0):
    isEquals = True

elif (arr[0]<0 and arr[2]>0) and (arr[1]<0 and arr[3]>0):
    isEquals = True

else:
    isEquals = True

if (isEquals):
    print("YES")
else:
    print("NO")