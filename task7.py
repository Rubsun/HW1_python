n = input()
skl1 = ['5', '6', '7', '8', '9', '0']
skl2 = ['2', '3', '4']
skl3 = ['11','12','13,','14','15','16','17','18','19']
word = 'korova'
if n[-1] in skl1:
    print(word[:5])
elif n[-1] in skl2:
    print(word[:5] + 'y')
elif n == '1':
    print(word)
elif n in skl3:
    print(word[:5])