sp='анна'
s='кактус'
def chek_polindrom(slovo):
    slovo_naoborot=slovo[::-1]
    if slovo_naoborot==slovo:
        print(slovo,'- полиндром')
    else: print(slovo,'- не полиндром')
chek_polindrom(sp)