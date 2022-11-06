#1 folosim change elements

'''1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
folosesc reverse pt inversare
'''

lista_note= ["do", "re", "mi", "fa","sol", "la", "si", "do"]
#suprascriere si inversare cu slicing
lista_note = lista_note[::-1]
print(lista_note)
#inversare cu metoda reverse
lista_note.reverse()
print(lista_note)

#2. De cate ori apare ‘do’?
print(lista_note.count('do'))

'''3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista. '''
#varianta 1 cu concatenare
lista_1 =[3, 1, 0, 2]
lista_2= [6, 5, 4]
lista_3 = lista_1 + lista_2
print(lista_3)
#varianta 2 cu extend
lista_1 =[3, 1, 0, 2]
lista_2= [6, 5, 4]
lista_1.extend(lista_2)
print(lista_1)

'''4.Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista'''

lista_3.sort()
print(lista_3)
lista_3.remove(0)
print(lista_3)

'''5. Folosind un if verificati lista generata la ex3 si afisati
Lista este goala
Lista nu este goala'''
if len(lista_3) >=1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#6. Folositi o functie care sa stearga lista de la ex3
del lista_3[0::]
print(lista_3)

'''7. Copy paste la ex 5. Verificati inca o data.
Acum ar trebui sa se afiseze ca lista e goala'''
if len(lista_3) >=1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

'''8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)
folosim keys'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

'''9. Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1)
print('Ana a luat nota',dict1['Ana'])
print('Gigel a luat nota', dict1['Gigel'])
print('Dorel a luat nota', dict1['Dorel'])

#10  Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6 (suprascriere)
dict1['Dorel']=6
# Printati nota dupa modificare
print('Nota lui Dorel dupa contestatie este:', dict1['Dorel'])


#11 Gigel se transfera din clasa
# Cautati o functie care sa il stearga (functia pop)
dict1.pop('Gigel')
print(dict1)

# Vine un coleg nou. Adaugati Ionica, cu nota 9
dict1['Ionica'] = 9
print(dict1)

'''12.Set
zile_sapt =  , 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt'''
zile_sapt = {'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add("luni")
print(zile_sapt)


'''13.Folositi un if si verificati daca 
Weekend este un subset al zilelor din sapt
Weekend nu este un subset al zilelor din sapt'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zile_sapt.')
else:
    print('Weekend nu este un subset al zile sapt.')

#14. Afisati diferentele dintre aceste 2 seturi
# ce contine A si nu contine b
print(zile_sapt.difference(weekend))
#ce contine B si nu contine A
print(weekend.difference(zile_sapt))
#functia symetric difference
print(zile_sapt.symmetric_difference(weekend))

#15.Afisati intersectia elementelor din aceste 2 seturi
zile_sapt = {'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
toate_zilele = zile_sapt.intersection(weekend)
print(toate_zilele)

'''16.Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise
Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea 
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python'''

#Declara o Lista cu 5 jucatori
echipa_mea=['Messi','Pique','Lewandowski','Pedri','Salah']

#Schimbari_efectuate = va jucati voi cu valori diferite
nume_jucator_schimbat=input('Numele jucatorului schimbat este:')
nume_jucator_intrat=input('Numele jucatorului care intra este:')

#3 Schimbari maxime admise
schimbari_maxime=int(input('Introdu un numar intre 0 si 3:'))

#Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
if nume_jucator_schimbat in echipa_mea:
    if 0<schimbari_maxime<3:
       echipa_mea.remove(nume_jucator_schimbat)
       echipa_mea.append(nume_jucator_intrat)
       print('A iesit', nume_jucator_schimbat, 'a intrat', nume_jucator_intrat, 'mai aveti', schimbari_maxime-1, 'schimbari.' )
    else:
        print('Nu se poate efectua schimbarea deoarece nu mai aveti schimbari.')
#Daca jucatorul nu e in teren:
if nume_jucator_schimbat not in echipa_mea:
        print('Nu se poate efectua schimbarea deoarece', nume_jucator_schimbat, ' nu este in teren.Mai aveti',schimbari_maxime,'schimbari.')


'''Google search hint
“how to check if item is in list python'''
#am gasit si cu functia any dar nu am stiut sa leg mai departe cu nr de schimbari

# Declara o Lista cu 5 jucatori
echipa_mea = ['Messi', 'Pique', 'Lewandowski', 'Pedri', 'Salah']
jucator_schimbat = input('Care este numele jucatorului:')

if any(jucator_schimbat in sublist for sublist in echipa_mea):
    print("Jucatorul este in teren")
else:
    print("Jucatorul nu este in teren")