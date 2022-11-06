import random

lista= ['mar', 'par', 'cirese', 'portocale']
for x in lista:
       lista.pop(1) #par este pop 1, apoi cirese devin pop 1
       print (lista)

for x in range(len(lista)):
       print(x)
#cand ne referim la index punem paranteze patrate

'''a. Usor (recomandat)
1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine. 
https://www.itfactory.ro/8174437-intro-in-programare/

Iteratiile sunt greute, deoarece necesita putina gandire algoritmica
Va rog sa imi scrieti pe slack unde intampinati dificultati si va ajut
Daca stati blocati > 30 min, cereti indiciu

b. Dificultate medie (Faceti cat puteti din ele)

1.
Avand lista 
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'] 

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while'''

#ex1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
'''Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x'''
for x in masini:
    print(f'Masina mea preferata este {x}')

#Faceti acelasi lucru cu un for each
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print(f'Masina mea preferata este {masina}')

#Faceti acelasi lucru cu un while
i = 0
while i <= len(masini)-1:
    print(f'Masina mea preferata este {masini[i]}')
    i += 1

'''2.Aceeasi lista
Folositi un for
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(1, len(masini)-1):
    masini[i] = masini[i].upper()
print(masini)

'''3. Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in masini: # for each daca nu tb sa modificam nimic in lista'''
    if i == 'Mercedes':
        print(f'Am gasit masina dorita de dvs')
        break
    else:
        print(f'Am gasit masina {i}. Mai cautam')
#intra in else cand i nu este Mercedes

'''4.Aceeasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
parcurgem lista cu for each, facem o verificare
folosim continue care iese din iteratia trabant or lastun, nu intra in for'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    else:
        print(f'S-ar putea sa va placa masina {masina}')

'''5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini adica x in masini
!!!!folosim in range pt ca am de facut o operatie pe lista!!!!!
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi cu append
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini) masini. replace (Tesla)
Printati Modele vechi: x
Modele noi: x'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

'''6. Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista'''

pret_masini = {"Dacia": 6800, "Lastun": 500, "Opel": 1100, "Audi": 19000, "BMW": 23000}
buget = int(input('\nCe buget aveti pentru masina? :'))
for masina in pret_masini:
    if buget >= pret_masini[masina]:
        print(f'Pentru un buget de {pret_masini[masina]} euro puteti alege masina {masina}')

'''7.Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
folosim o variabila noua, folosim for each pt a itera prin lista'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)
total=0
for numar in numere:
    if numar == 3:
        total += 1
print(f'\nNumarul 3 apare de {total} ori.', end="")


'''8. Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)'''
s=0
numere = [3, 7, 10, 20, 30]
for numar in numere:
    print(f'numarul curent este{numar}')
    s=s+ numar
    print(f'suma este {s}')


'''9. Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)'''
numere = [3, 7, 10, 20, 30]
nr_max = 0
for numar in numere:
    if numar > nr_max:
        nr_max = numar
print(f'\nCel mai mare numar din lista este {nr_max}.')

'''10.Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista'''
numere = [3, 7, 10, 20, 30]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = numere[i] * -1
print(f'\nNoua lista este: {numere}')



'''c. Optionale (may need google)

11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere 
Populati corect celelalte liste
Afisati cele 4 liste la final

parcurgem lista cu for each pt ca avem nevoie doar de valorile din lista
folosim prima data if pt conditia nr pozitive >=0
folosim 2 if else ca sa verifice toate criteriile'''

numere2 = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

num_pare = []
num_impare = []
num_poz = []
num_neg = []
for numar in numere2:
    if numar >= 0:
        num_poz.append(numar)
    else:
        num_neg.append(numar)
    if numar % 2 == 0:
        num_pare.append(numar)
    else:
        num_impare.append(numar)
print(f'\nListele sunt:\n Numere pozitive: {num_poz};\n Numere negative: {num_neg};'
      f'\n Numere pare: {num_pare};\n Numere impare: {num_impare}.')



'''12.
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
https://www.youtube.com/watch?v=lyZQPjUT5B4
metoda cea mai cunoscuta folosim 2 iteratoare: i si j'''
numere2 = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
aux = 0
for i in range(len(numere2)):
    for j in range(i + 1, len(numere2)):
        if numere2[i] > numere2[j]:
            aux = numere2[i]
            numere2[i] = numere2[j]
            numere2[j] = aux
print(f'\n{numere2}')


'''13.ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!'''

numar_random = random.randint(1, 30)
print("numarul de ghicit e ", numar_random)
numar_ghicit=''
while numar_random != numar_ghicit:
    numar_ghicit = int(input('\nGhiceste numarul: '))
    if not numar_ghicit in range(1,31):
        print('Numarul trebuie sa fie intre 1 si 30!')
    elif numar_ghicit < numar_random:
        print('Nr secret e mai mare!')
    elif numar_ghicit > numar_random:
        print('Nr secret e mai mic!')
    else:
        print('Felicitari! Ai ghicit!')

'''14. 
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333'''
n = int(input('\nIntroduceti un numar mai mic decat 10: '))
for x in range(1, n + 1):
    print(x*str(x))

'''15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)'''


tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta e {tastatura_telefon[i][j]}')

