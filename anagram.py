#word = input('Wprowadz slowo: ').lower() mozna tez wrzucic od razu metode do zmiennej
word = input('Wprowadz slowo: ')
word = word.lower() #lower zamienic slowo na male litery, wykonac metode na niej i zapisz pod ta sama zmienna

no_of_reps = len(word) // 2 #czesc calkowita z dzielenia
points = 0

for i in range(no_of_reps):
    print(f'porownanie {i+1}')
    print(f'porownuje {word[i]} z {word[-1-i]}')
    if word[i] == word[-1-i]:
        print('Ok, znaki pasuja')
        points += 1
    else:
        print('NOK - nie sa takie same')
        break #wychodze z petli, jesli sie chociaz 1 rzecz nie zgodzi to nie bedzie robil juz tej petli

if points == no_of_reps:
    print('slowo jest anagramem')
else:
    print('to slowo nie jest anagramem')



#anagram 2 
#krotszy zapis spr. od tylu

'''
sample = 'Konstantynopol'
print(sample[1]) #znak jakis ze slowa
print(sample[4:7]) #kawalek ze slowa
print(sample[1:8:2])  #skacze co druga literka jak w petli od, do krok
print(sample[:8:2]) #jesli jest puste peirwsze do od pcozatku do 0
print(sample[1::2]) # jesli puste 2 to znaczy ze do konca
print(sample[10:2:-2])  #od 10 do 2 co drugi od tylu

print(sample[::-1])
'''

word = input('Wprowadz slowo: ')
word = word.lower()

if word == word[::-1]: #slowo sprawdzane od konca
    print('To jest anagram')
