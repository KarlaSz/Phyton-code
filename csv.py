#csv

#1 odczyt csv z zapisem poszczegolnych pol bez bubliotek bo mozna tez z pandas to zrobic

#mode w jakim trybie np. do odczytu
#path sciezka

# with open('rozliczenie.csv', 'r') as file1: # po as daje swoja nazwe pliku jaka chce
#jak jestem w wcieciu to plik jest otwarty , jestem w nim, metoda open otwiera i zamyka plik sama


path = 'rozliczenie.csv'
mode = 'r' #read
with open(path, mode) as file_csv:
    content = file_csv.readlines()
print(content)
print(content[4])
for i in range(len(content)):
    print(f'przed: {content[i]}')
    content[i] = content[i].split(';')
    print(f'po: {content[i]}')
print(content)    # wszystko
print(content[3]) # jeden wiersz
print(content[3][2])   #pierwsze to wiersz,a drugi o kolumnie mowi
print('Koniec części 1\n')

# przeczytaj ten plik i zapisz go do zmiennej i wyswietl jako 1 string
# w read mozna podac ile znakow wyswietlic jako parametr
# readline czyta cale wiersze
# jak jestem w wcieciu to plik jest otwarty i mozna go edytowac, a jak printa dam poza to jest zamkniety


for i in range(len(content)):
    print((f'przed: {content[i]}'))
    content[i] = content[i].split(',') #wez konkretna linie i wez splita i podziel ja po przecinku i zapisz do zmiennej
    print((f'po: {content[i]}'))
   # print(content)  # wszystko
    #print(content[3])  # jeden wiersz
    #print(content[3][2]) # jedna komórka, #pierwsze to wiersz,a drugi o kolumnie mowi


#2 oblicz srednia wyplate


#for i in range (1,len(content)): #nie od 0 od pierwszego wersza gdzie jest wyplata tylko od 2
 #   print(content[i][1])

total = 0

for line in content[1:]:  #nie bierz calej calej taebli tylko od lini z indeksem 1 az do konca
    total += int(line[1])
print(f'srednia wyplata to {total / len(content)-1}')
#jak jest w srodku bloku petli to sie w nieskonczonosc wykonuje tyle ile wierszy,a jak poza to dla calej petli wynik


#3 ile kobiet jest na macierzynskim?

count = 0
for line in content[1:]:
    line[4] = line[4].replace('\n', '') #spr. przypadek gdyby pozycja kolumny w wierszu sie zmienila po zawarctosi
    if line[4].lower() == 't' and line[3] == 'k':
        count += 1
print(f'{count} kobiety na macierzynskim')

'''
macierzysnki = 0
for i in range (1,len(content)): #nie od 0 od pierwszego wersza gdzie jest wyplata tylko od 2
     print(content[i][4])
     if content[i][4] == 't\n':
        macierzysnki += 1
print('na macierzynskim jest:',macierzysnki, 'kobiet')
'''
