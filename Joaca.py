'''22. Joc ghicit zarul
Cauta pe net si vezi cum se genereaza un numar random
Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
Luati un nr ghicit de la utilizator
Verificati si afisati daca utilizatorul a ghicit
3 optiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
Ai ghicit. Felicitari? Ai ales x si zarul a fost y'''

import random

dice_roll = random.randint(1,6)
b= int(input('Numarul ghicit de utilizator este:'))
while dice_roll!=b:
#este diferite de b
    if dice_roll > b:
        print('mai mare')
    else:
        print('mai mic')
    break
else:
    print('ai ghicit numarul')


'''20. avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
if lower primul caracter = upper primul caracter etc'''


lista =[0,1,2,3,4,5,6,7,8,9]
#iterator
#parcurgem lista si tb sa vedem cand iesim din lista.Iese cand ajunge la val 10 de asta implementam i =i+1
i= 0
while i <len(lista):
    i=i+1
#putem scrie i+ = 1
    if i%2==0:
        print(i)

print('for')
for i in range(4):
    print(i)

firme = ['kfc', 'mcdonalds', 'subway']
for x in firme:
    print (x)

#itereaza cheile pe rand si printeaza valorile, x contine cheile in exemplul de mai jos
dict = {
    "masina" : "dacia",
    "casa" : "mare"
}
for x in dict.keys():
    print (dict[x])


print('for each')
logo = 'apple'
for x in logo:
    print (x)


dict = {
    "masina" : 'dacia',
    "casa":"mare"
}
for x in dict.keys():
    if dict [x] == 'dacia':
        break
    print (x)


