#metody

# funkcje to np. print(), czyli nazwa i () czasami z parametrami, round()

# metody widoczne sa po kropce, takie funkcje sa wspierane dla danego typu
napis = 'piesek'

liczba = 5

print(napis.upper())
#print(napis.replace(__old='s',__new='d'))

zdanie = 'Ala ma kota i go nie lubi'
print(zdanie.split()) #dzieli wzgledem spacji
print(zdanie.split('a')) #podzielenie zdanie

zdanie2 = 'Kamil,Magda,Bartek,Kasia'
#zdanie2 = zdanie2.split() #wykonaj splita na tym i nadpisz na tej samej zmiennej
print(zdanie2.split()) #dzieli wzgledem spacji
print(zdanie2.split(',')) #dzieli wzgledem przecinka

#sposob na cudzyslow
#print('It\'s cool')