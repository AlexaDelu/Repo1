#ex 18
import random

text='Coral is either the stupidest animal or the smartest rock'
x = slice(5)
print (text[x])

#slice printeaza primele 5 caractere in acest ex


#c. Optionale (may need google)

'''11.Verifica daca x are minim 4 cifre (x e int)
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)'''
x = int(input('Numarul x este: '))
if(len(str(x)) >= 4):
    print('X are minim 4 cifre')
else:
    print('X nu are minim 4 cifre')

#12.Verifica daca x are exact 6 cifre
x = int(input('Numarul x este:'))
if(len(str(x)) == 6):
    print('X are 6 caractere')
else:
    print('X nu are 6 caractere')

'''13.
Verifica daca x este numar par sau impar (x e int)'''
x = int(input('Numarul x este:'))
if(x%2== 0):
    print('x este numar par')
else:
    print('x este numar impar ')

'''14.
x, y, z (int)
Afiseaza care este cel mai mare dintre ele?
functia max
print max(x,y,z)
sau pe bucati '''
x = int(input('Numarul x este:'))
y = int(input('Numarul y este:'))
z = int(input('Numarul z este:'))
if(x>y and x>z):
    print('x este cel mai mare dintre ele')
elif(x<y and y>z):
    print('y este cel mai mare dintre ele')
elif(x<z and y<z):
    print('z este cel mai mare dintre ele')
elif(x==y<z):
    print('z este cel mai mare dintre ele')
elif(x>y==z):
    print('x este cel mai mare dintre ele')
elif(y>x==z):
    print('y este cel mai mare dintre ele')


'''15. 
X, y, z - reprezinta unghiurile unui triunghi
Verifica si afiseaza daca triunghiul este valid sau nu
#suma unghiurilor tb sa fie 180- x+y+z'''
x = int(input('Numarul x este:'))
y = int(input('Numarul y este:'))
z = int(input('Numarul z este:'))
if((x+y+z)==180):
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

'''16. 
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
x= int input
printare a (stringul dat) si slincing (0 pana ce nr alegem noi)'''
a='Coral is either the stupidest animal or the smartest rock'
x=int(input('Numarul x este:'))
print(a[0:-x])


'''17.
acelasi string
declara un string nou care sa fie format din primele 5 caractere + ultimele 5
b= string a de la 0 pana 5
:- inseamna pana la ultimul caracter'''
vechi='Coral is either the stupidest animal or the smartest rock'
nou= vechi[0:5] +vechi[len(vechi)-5::]
print(nou)


'''18.
acelasi string
salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' 
functia index'''
text = 'Coral is either the stupidest animal or the smartest rock'
start_index = text.find('rock')
print(start_index)
print(f'{text[0:start_index]}')

'''19. 
citeste de la tastatura un string
verifica daca primul si ultimul caracter sunt la fel
se va folosi un assert
atentie: se doreste ca programul sa fie case insensitive
'apA' e acceptat'''

'''20. 
avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
if lower primul caracter = upper primul caracter etc'''


'''Bonus la cerere:
21.
Verificare imbarcare persoane
Tineti urmatoarele date
Varsta
Insotit de mama
Insotit de tata
Pasaport
Act permisiune mama
Act permisiune tata

Conditii de imbarcare
Daca pers are varsta peste 18 ani si are pasaport
Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte

Aici vreau sa testati codul cu toate variantele posibile
Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results

Ex:
Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
Etc
cu assert'''
varsta = int(input('Introdu varsta copilului\n'))
insotit_de_mama = bool(input('Introdu TRUE/False daca merge cu MAMA\n'))
insotit_de_tata = bool(input('Introdu TRUE/False daca merge cu TATA\n'))
pasaport = bool(input('Introdu Introdu TRUE/False daca ai pasaport\n'))
act_permisiune_mama = bool(input('Introdu TRUE/False daca ai Permisiune de la Mama\n'))
act_permisiune_tata = bool(input('Introdu TRUE/False daca ai Permisiune de la Tata\n'))

if varsta >= 18 and pasaport is True :
    print(f'Persoana are {varsta} am pasaport.Ma pot imbarca')
elif varsta < 18:
    if pasaport is True :
       if  insotit_de_mama is True and insotit_de_tata is True :
           print(f'Persoana are {varsta} ani merge cu Mama si Tata. Se poate imbarca.')
           if insotit_de_mama is True and act_permisiune_tata is True :
               print(f'Persoana are {varsta} ani merge cu Mama, are permisiune. Se poate imbarca.')
               if insotit_de_tata is True and act_permisiune_mama is True :
                  print(f'Persoana are {varsta} ani merge cu TATA si are permisiune.Se poate imbarca.')
                  if insotit_de_mama is False or insotit_de_tata is False :
                      print(f'Persoana are {varsta} ani nu merge insotit . NU se poate imbarca!')
                      if insotit_de_mama is True and act_permisiune_tata is False :
                          print(f'Persoana are {varsta} ani  merge insotit dar nu are permisiunea parintelui. NU se poate imbarca!')
                          if insotit_de_tata is True and act_permisiune_mama is False :
                               print(f'Persoana are {varsta} ani merge insotit dar nu are permisiunea parintelui. NU se poate imbarca!')
    if pasaport is False :
        print(f'Persoana are {varsta} ani,nu are pasaport, NU se poate imbarca')
else:
      print('Nu am pasaport, Nu ma pot imbarca')

'''22. Joc ghicit zarul
Cauta pe net si vezi cum se genereaza un numar random
Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
Luati un nr ghicit de la utilizator
Verificati si afisati daca utilizatorul a ghicit
3 optiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
Ai ghicit. Felicitari? Ai ales x si zarul a fost y'''

from random import random

dice_roll = random()
numar_utilizator = int(input('Ce numar alegi?\n'))
if dice_roll == numar_utilizator:
    print('Egalitate!')
elif numar_utilizator == 1 and numar_utilizator < dice_roll:
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {numar_utilizator}, iar computerul {dice_roll}')
elif numar_utilizator == 2 and numar_utilizator < dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {numar_utilizator}, iar computerul {dice_roll}')
elif numar_utilizator == 3 and numar_utilizator < dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {numar_utilizator}, iar computerul {dice_roll}')
elif numar_utilizator == 4 and numar_utilizator < dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {numar_utilizator}, iar computerul {dice_roll}')
elif numar_utilizator == 5 and numar_utilizator< dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {numar_utilizator}, iar computerul {dice_roll}')
elif numar_utilizator <= 6 and numar_utilizator > dice_roll :
    print(f'Ai castigat! Ai ales un numar mai mare. Ai ales: {numar_utilizator}, iar computerul {dice_roll}')
else:
    print(f'Introdu un nr de la 1 - 6. Ai ales: {numar_utilizator}.')
