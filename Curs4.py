#cicluri repetitive
#while este un loop sau un ciclu repetitiv-zona de cod care se repeta atat timp cat o conditie e true
#iteratia se pune mereu la final

litri_benzina = 10
while litri_benzina > 0:
    # accelerare
    print('vrum vrum')
    # va printa continuu pt ca nu are o oprire
    # scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print("beculet rosu")
print('stop')

# dalmatienii
# intra si imi printeaza toate numerele de la 0 la 101
for i in range(1, 102):
    print(f'dalmatianul cu nr{i}')

# putem printa dalmatienii din 2 in 2 spre ex, ultimul argument fiind pasul adica din cat in cat vrem sa printam in ex de mai jos 2
#!!!!folosim in range cand avem de facut o operatie pe lista!!!!!
for i in range(1, 102, 2):
    print(f'dalmatianul cu nr{i}')

numere = [3, 7, 10, 20, 30]
# parcurgere lista cu for prin intermediul indexului
for i in range(0, len(numere)):
    print(f'indexul curent este {i}')
#daca vrem sa printam numerele vom scrie asa
    print(f'numarul curent este {numere[i]}')

# i este iterator
x = 10
y = 5
while x> 0 and y>0:
    print(x+y)
    x-=2
    y-=1
else:
    print('valorile lui x si y sunt')

#dif intre if si while la else este ca la while intra oricum else la final , se executa dupa ce se termina condt din while.
#else intra automat nu ca la if unde intra doar daca nu era indeplinita condt

#while -break
x = 10
while x> 0 and y > 0:
    print(x)
#intervine break si zice sa iesi de tot din while, printeaza 10 aici
    if x == 4:
        break
        x-=2
        y-=1

#while-continue
print('continue')
y = 8
while y > 4:
    if y == 6:

        print(y)
#exclude valoarea 6 din loop si printeaza restul


lista =[0,1,2,3,4,5,6,7,8,9]
#iterator
#parcurgem lista si tb sa vedem cand iesim din lista.Iese cand ajunge la val 10 de asta implementam i =i+1
i= 0
while i <len(lista):
    i=i+1
#putem scrie i+ = 1
    if i%2==0:
        print(i)


#for/for else
#se executa un bloc de cod pt fiecare valoare din range
#e folosit pt a parcurge liste,dictionare,tuple


#for each
#parcurge pas cu pas fiecare caracter din tot stringul, printeaza fiecare caracter pe rand si la final iese
print('for each')
logo = 'apple'
for x in logo:
    print (x)

#for each
# for each daca nu tb sa modificam nimic in lista
numere = [3, 7, 10, 20, 30]
for numar in numere:
    print(f'numarul curent este{numar}')

#putem printa suma
numere = [3, 7, 10, 20, 30]
s=0
numere = [3, 7, 10, 20, 30]
for numar in numere:
    print(f'numarul curent este{numar}')
    s=s+ numar
    print(f'suma este {s}')

#parcurge fiecare elem si il printeaza
firme = ['kfc', 'mcdonalds', 'subway']
for x in firme:
    print (x)

dict = {
    "masina" : 'dacia',
    "casa" :"mare"
}
for x in dict.keys():
    print (dict(x))

#for break
#Iesim din ciclu folosind un cuvant cheie care face acest lucru, adica break
print('for -break')
dict = {
    "masina" : 'dacia',
    "casa" :'mare'
}
for x in dict.keys():
    if dict [x] == 'dacia':
        break
    print (x)


#daca gaseste x nu il printeaza, printeaza tot cu exceptia mcdonalds in ex de mai jos
#continue e un fel de skip, nu mai continua sa execute
print ('for continue')
firme = ['kfc', 'mcdonalds', 'subway']
for x in firme:
    if x == 'mcdonalds':
    continue
    print(x)


for i in range (3,10,2):
    print i

# !!!!! cand tb sa facem op pe lista folosim in range
#\n inainte de ce scriem la printaare adauga o linie
