#funkcje
#program liczby BMI osoby

def welcome(name):
    print(f'Witaj {name}')
    print(f'Trwa zakladanie maila {name}@gmail.pl')
    print('Zglos sie do recepcji')

welcome('Karolina')


def BMI(wzrost, waga):
    result = waga / (wzrost**2) #kwadrat do potegi 2
    return round(result,2)

waga = int(input('Podaj wage w kg '))
wzrost = float(input('Podaj wzrost w m '))
print(BMI(wzrost,waga))