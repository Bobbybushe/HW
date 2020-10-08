while True:
    sign=input('Введите знак: ')
    if sign=='0':
        break
    if sign in ('+', '-', '/', '*'):
        x = float(input('Введите число1: '))
        y = float(input('Введите число1: '))
        if sign=='+':
            print(x+y)
        elif sign=='-':
            print(x-y)
        elif sign=='*':
            print(x*y)
        elif sign=='/':
            if y!=0:
                print(x/y)
            else: print('Деление на 0!')
    else: print('Неверный знак')


