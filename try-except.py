slowo = 'mama'
try:
    print(slowo[6])
except:
    print('Nie da się')
    print(slowo[-1])

a, b = 3, 0
try:
    wynik = a / b
except:
    wynik = 0




print(wynik + 3)


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


#druga czesc

x = input('Wprowadz wartosc: ')

try:
    x = int(x)
    print(f'{x} jest intem')
except:
    try:
        x = float(x)
        print((f'{x} jest floatem'))
    except:
        print(f'{x} zostaje stringiem')