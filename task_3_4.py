s = input('Введите строку ')
sl=len(s)/2
print(s[int(sl)])
if s[int(sl)] == s[0]:
    sn=s[1:-2]
    print(sn)