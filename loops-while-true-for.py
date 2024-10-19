wiek = int(input('Ile masz lat? '))


if wiek < 18: #: ze bedzie warunek i wciecie 
    print('Bedziesz pelnoletni za', 18-wiek,'lat') #wchodzi tu jesli spelnia warunek tylko i wchodzi tu
else:
    print('Jestes dorosly')
print('Koniec programu') #to sa pytanie poza warunkami i sie zawsze wykonuja

#print('Wychodze z programu')




zarobki = float(input('Ile zarabiasz? '))

if zarobki > 5000:
    print('Podatek 20%, na rękę', zarobki * 0.8)
    print('Jestes bogaty')
elif zarobki > 3000:
    print('Podatek 10%, na rękę', zarobki * 0.9)
    print('Niski podatek')
elif zarobki >= 0:
    print('Podatek 0%, na rękę', zarobki)
    print('Zwolniony z podatku')
elif zarobki == 0:
    print('Nie zarabiasz, nie ma podatku')
else:
    print('niepoprawna kwota ')
print('dalsza czesc')


#uwazac na wciecia bo maja znaczenie w wysswietlaniu 

passwd = input('Podaj haslo ')

if passwd != '1234':
    print('brak dostepu')
else:
    print('haslo poprawne')
    print('wejscie do systemu')

#while petle 

'''
x = int(input('Ile razy chcesz wykonac kod?  '))

#wykonuj tak dlugo az spelnisz warunek
while x >= 0:
    print('Lecimy')
    x = x -1
    print('x wynosi', x)
print('Koniec programu')


passwd = input('Podaj haslo:  ')
while passwd != 'Piesek':
    passwd = input('Jeszcze raz:  ')
print('Witamy w programie')
'''

#program pyta o liczbe dni urlopu, ktore pracownik chce wykorzystac
#program przyjmuje liczby od 1 do 99

'''
urlop = int(input('ile dni urlopu chcesz wziac?  '))

while urlop < 1 or urlop > 99:
    print('zla wartosc, jeszcze raz')
    urlop = int(input('Jeszcze raz:  '))
print('OK, masz urlop')
#0 > urlop <= y inny warunek
'''

'''
if y >= 1:
    print('urlop przyznany')
elif y <= 99:
    print('urlop przyznany')
else:
    print('nie tym razem')
'''

#program pyta o liczbe dni urlopu, ktore pracownik chce wykorzystac
#program przyjmuje liczby od 1 do dostepnych dni urlopu

dostepny_urlop = int(input('Ile masz dni urlopu? ' ))
urlop = int(input('ile dni urlopu chcesz wziac?  '))    

while urlop < 1 or urlop > dostepny_urlop:
    print('zla wartosc, jeszcze raz')
    urlop = int(input('ile dni urlopu chcesz wziac?  '))
print('OK, masz urlop')
print('Zostalo', dostepny_urlop - urlop, 'dni')
    

#while true - logiczna prawda, krec sie caly czas,az do przerwy az zostanie spelniony i losujemy warunki jaki chcemy. kreci sie tyle razy az sie cos stanie

#wez petle i lec z nia w nieskonczona i w srodku petli mozemy dac mu komende wyjdz
# i lec dalej

print('witamy w panelu logowania')
while True:
    user = input('Wprowadz nazwe uzytkownika:  ')
    passwd = input('Wprowadz haslo:  ')
    if user == 'Karolina' and passwd == 'Bony':
        print('Poprawne dane, witaj', user)
        break
    elif passwd == 'serwis':
        print('Wprowadziles haslo serwisowe')
        break #wyjscie z petli
    else:
        print('Niepoprawne dane logowania, jeszcze raz')
print('uzytkownik zalogowany')


#petle true zad kolejne

while True:
    x = int(input('Podaj dodatnią liczbę '))
    if x > 0:
        break
print('Dalsza czesc programu')


#program losuje liczb / ma liczbe 
#uzytkownik zgaduje liczbe, a program pisze, czy zgadywana liczba jest wieksza, mniejsza czy rowna 

while True:
    liczba = int(input('losuj liczbe '))
    user_liczba = int(input('losowa liczba to '))
    if user_liczba > liczba:
        print('liczba jest wieksza')
        break
    elif user_liczba < liczba:
        print('liczba jest mniejsza')
        break
    elif user_liczba == liczba:
        print('liczba jest rowna')
        break
    else:
        print('innym razem')


#rozbudowana wersja 

import random #importowanie biblioteki random 
a = int(input('Od jakiej liczby losujemy?  '))
b = int(input('Do jakiej liczby losujemy? '))
#liczba = random.randint(0, 10)
liczba = random.randint(a, b)

print('Wylosowalem liczbe z przedzialu',a,',',b)
count = 0 

while True:
    #liczba = int(input('losuj liczbe '))
    if count == 3:
        print('Przekroczona liczbe prob')
        break
    user_liczba = int(input('zgadnij liczbe '))
    if user_liczba > liczba:
        print('Twoja liczba jest wieksza, nie zgadles')
    elif user_liczba < liczba:
        print('Twoja liczba jest mniejsza, nie zgadles')
   # elif user_liczba == liczba:
    #   print('liczba jest rowna, BRAWO, zgadles!')
    #    break
    else:
        print('Zgadles')
        break
    count += 1 

print('Wylosowalem liczbe z przedzialu',a,',',b)
count = 0 

while True:
    #liczba = int(input('losuj liczbe '))
    user_liczba = int(input('zgadnij liczbe '))
    count += 1
    if count == 3:
        print('Przekroczona liczbe prob')
        break
    if user_liczba > liczba:
        print('Twoja liczba jest wieksza, nie zgadles')
    elif user_liczba < liczba:
        print('Twoja liczba jest mniejsza, nie zgadles')
   # elif user_liczba == liczba:
    #   print('liczba jest rowna, BRAWO, zgadles!')
    #    break
    else:
        print('Zgadles')
        break

#petla for - kreci sie tyle razy ile chcemy



#i iteracja ktroy zmienia wartosc
#range zakres ile razy ma sie krecic
for i in range (5):
    print(i)


'''
lista = ['marchew', 'sok', 'jablko', 'budyn'] 
print(lista)
print(lista[0])
print(lista[-1]) #jak nie wiem ile elementow nie wiem ile mam to moge od tylu leciec 
print(lista[1])
print(len(lista))
'''
'''
slowo = 'konkatowac'
print(slowo[2])
#print(slowo[15]) #poza zasiegiem 
'''


#szukanie literki





slowo = 'Wokabularz'
count = 0
for i in range(len(slowo)):
    print(slowo[i])
    if slowo[i] == 'a':
        print('znaleziona literka "a"')
        count += 1
print('literka wystepuje',count,'razy')
    #ile razy wsytepuje litera a 
print(len(slowo))


'''
slowo = 'dupa'
count = 0
for i in range(len(slowo)):
    print(slowo[i])
    if slowo[i] == 'a':
        print('znaleziona literka "a"')
        count += 1
print('literka wystepuje',count,'razy')
    #ile razy wsytepuje litera a 
    
#print(len(slowo)) #sprawdza dlugosc len slowa 


--
#szuka 

#szuka danych w tablicy
lista = ['marchew', 'sok', 'jablko', 'budyn'] 
count = 0 

for i in range(1):
    print('ile jest produktow w liscie:',len(lista))
    
for i in range(len(lista)):
  #  print(i+1,'slowo to', lista[i],', wiec to slowo ma',len(lista[i]),'liter') ze spacja
    print(f'{i+1} slowo to {lista[i]}, wiec to slowo ma {len(lista[i])} liter')
    if len(lista[i]) > 4:
      #  lista[i] = '####'
        count += 1
    print('liczba dlugich slow', count)

--
petla for z przedzialami do do i krokiem

for i in range(3,19,4): #od do z krokiem czyli co ile
    print(i)
    
for i in range(100,5, -1):
    print(i)

import random
for i in range(100,5, random.randint(-15,-2)):
    print(i)

'''
auta = ['Audi', 'BMW', 'Toyota', 'Fiat', 'Skoda']

# to leci z zakresu auta i dlugosci tablicy
for i in range(len(auta)):
    print('prezentuje wam:',i)

#od razu w elemencie, prosztszy zapis, bez range
for auto in auta: 
   print('prezentuje panstwu',auto) 