z=input('Введите число ')
summ=0
for i in range(len(z)):
    summ+=int(z[i])
print('Сумма чисел ',summ)
proiz=1
for i in range(len(z)):
    proiz*=int(z[i])
print('Произведение чисел ', proiz)