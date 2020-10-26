def sm_t_d(a):
    b=a*0.394
    return b
def d_t_sm(a):
    b=a/0.394
    return b
def mi_t_km(a):
    b=a*0.621
    return b
def km_t_mi(a):
    b=a/0.621
    return b
def f_t_kg(a):
    b=a*2.205
    return b
def kg_t_f(a):
    b=a/2.205
    return b
def y_t_gr(a):
    b=a*0.0353
    return b
def gr_t_y(a):
    b=a/0.0353
    return b
def gr_t_y(a):
    b=a/0.0353
    return b
def gal_t_l(a):
    b=a*3.785
    return b
def l_t_gal(a):
    b=a/3.785
    return b
def pint_t_l(a):
    b=a*0.473
    return b
def l_t_pint(a):
    b=a/0.473
    return b
print('1 - Дюймы в сантиметры')
print('2 - Сантиметры в дюймы')
print('3 - Мили в километры')
print('4 - Километры в мили')
print('5 - Фунты в килограммы')
print('6 - Килограммы в фунты')
print('7 - Унции в граммы')
print('8 - Граммы в унции')
print('9 - Галлоны в литры')
print('10 - Литры в галонны')
print('11 - Пинты в литры')
print('12 - Литры в пинты')
print('0- Выход')
while True:
    z=input('Выберите перевод: ')
    if z=='0':
        break
    if z in ('1','2','3','4','5','6','7','8','9','10','11','12'):
        b=0.0
        a=int(input('Введите количество: '))
        if z=='1':
            b=d_t_sm(a)
            print(b,'см')
        elif z=='2':
            b=sm_t_d(a)
            print(b,'д')
        elif z=='3':
            b=mi_t_km(a)
            print(b,'км')
        elif z=='4':
            b=km_t_mi(a)
            print(b,'мили')
        elif z=='5':
            b=f_t_kg(a)
            print(b,'кг')
        elif z=='6':
            b=kg_t_f(a)
            print(b,'фунтов')
        elif z=='7':
            b=y_t_gr(a)
            print(b,'гр')
        elif z == '8':
            b = gr_t_y(a)
            print(b, 'унций')
        elif z=='9':
            b=gal_t_l(a)
            print(b,'литров')
        elif z=='10':
            b=l_t_gal(a)
            print(b,'галлонов')
        elif z=='11':
            b=pint_t_l(a)
            print(b,'л')
        elif z=='12':
            b=l_t_pint(a)
            print(b,'пинт')
    else: print('Неизвестный идентификатор')
