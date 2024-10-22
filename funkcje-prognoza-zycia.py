#funkcja

#funkcja ktora przyjmuje: wiek, plec, stan zdrowia
#funkcja zwraca prognoze, jak dlugo jeszcze bedzie zyl user

'''
wiek = int(input('podaj wiek '))
plec = input('podaj plec ')
zdrowie = int(input('ocen zdrowie od 1 do 5 '))
print(prognoza(wiek,plec,zdrowie))
'''


def prognoza(wiek, plec, zdrowie):
    if plec.lower() == 'k':
        result = (90 - wiek) * zdrowie / 100
    elif plec.lower() == 'm':
        result = (77 - wiek) * zdrowie / 100
    else:
        result = 2
    return result


#dane = input('Wprowadz wiek, plec, stan zdrowia ').split()
#print(prognoza(int(dane[0]), dane[1], int(dane[2])))

#podejsice iteracyjne
def silnia1(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
        print(i)
    return wynik

print(f'silnia z 5 to: {silnia1(5)} ')


#podejscie rekurencyjne

def silnia2(n):
    if n == 1:
        return 1
    else:
        return n * silnia2(n-1)
print(silnia2(5))