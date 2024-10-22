#petla for 

#mamy liste imion
#program ma napisac dlugosc imion i napisac przywitanie TYLKO dla mezczyzn

names = ['Przemek', 'Paulina', 'Karolina', 'Adam', 'Iza']

for name in names:
    print(f'Imie {name} ma {len(name)} liter.') # f to format, inny sposob zapisu 
    if name[-1] == 'a':
        continue
    print(f'Witam Pana, Panie {name}')