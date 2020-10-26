n=16
def fuct2(n):
    sp = []
    if n%2==0:
        for i in range(2, n+1, 2):
            sp.append(i)
        fn=1
        print(sp)
        for i in range(len(sp)):
            fn=fn*sp[i]
        return print('двойной факториал',n,'=',fn)
    else:
        for i in range(1, n+1, 2):
            sp.append(i)
        print(sp)
        fn = 1
        for i in range(len(sp)):
            fn = fn * sp[i]
        return print('двойной факториал', n, '=', fn)
fuct2(n)

