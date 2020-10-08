a = input('Введите количество гостей')
if int(a) > 50:
    print('Ресторан')
elif int(a) >= 20 and int(a) <= 50:
    print('Кафе')
elif int(a) < 20:
    print('Дом')