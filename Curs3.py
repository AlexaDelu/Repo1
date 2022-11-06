#structuri de date

'''lista- mai multe valori de date (string, boolean,float,integer etc) inmagazinate intr-o sg variabila
se bazeaza pe indexuri incepand de la 0,este mutabila-putem sterge ,adauga,schimba
len() ne va da dimensiunea listei
cand adaugam un element nou acesta se duce la sf listei-lista este ordonata
#in lista putem pune valori duplicate'''

lista_mea = ["masina", "casa", True, 22, 67.6]
#lista de mai sus are 5 elemente, ele se despart prin virgula
#masina este elem 0, casa este elem 1 etc


#operatii cu liste
#index
#va afisa elem masina
print(lista_mea[0])

#slicing
print((lista_mea[1:3]))
#merge de la 1 pana la 3, dar nu afiseaza si a patra valoare
#daca vrem sa sara ceva punem :

#daca punem direct 2 puncte ne ia de la inceputul listei
print((lista_mea[:]))

#daca punem minus 1 imi arata toata lista mai putin ultimul element din lista
print(lista_mea[:-1])

if True in lista_mea:
    print('succes')
#poti sa pui condt sa gaseasca element in lista -in cazul asta True daca e in lista se printeaza succes


#suprascriem un element- ii dam nr care corespunde pt a inlocui acel elem
lista_mea [0] = 'apartament'

#append
lista_mea.append("4")
print(lista_mea)

##putem adauga orice, nu numai string cum este 4 mai jos
lista_mea.append(4)

#insert
#putem adauga element oriunde in lista, aici am pus 1 in fata deci imi adauga la pozitia 2 mancare
lista_mea.insert(1, "mancare")
print(lista_mea)

#extend- adaugam lista la lista, chiar si cu element dublat
lista_2 = ["masline", 4]
lista_mea.extend(lista_2)
print(lista_mea)

#remove-dispare elementul din lista
lista_mea.remove( 'masina')
print(lista_mea)

#pop- elimina indexul cu nr pe care il scrii, in cazul nostru indexul 1 adica mancare
# scoate si returneaza ultimul element
last = lista_mea.pop()
lista_mea.pop(1)
print(lista_mea)

#daca nu punem niciun nr imi scoate ultimul element
lista_mea.pop()
print(lista_mea)

#del- este un key word cum sunt toate cu portocaliu, sterge complet lista
#del lista_mea
#print(lista_mea)

#clear sterge doar elementele din lista, lista ramane
#lista_mea.clear()
#print(lista_mea)

#sort tb sa avem elemente de acelasi tip
#lista_2.sort()
#print(lista_2)

#copy-copiaza lista
lista_ta = lista_mea.copy()
print(lista_ta)

#list copiaza dintr-o lista in alta
lista_3 = list(lista_2)

#concatenare
lista_4 = lista_2 + lista_3
print(lista_4)

#extend se adauga la lista stabilita elemente, in cazul nostru lista_mea
lista_mea.extend(lista_2)
print(lista_mea)

#type-afli tipul, clasa
print(type(lista_mea))

#len-nr de elemente,dimensiunea in cazul nostru 9
print(len(lista_mea))

#count-de cate ori apare un element intr-o lista
print(lista_mea.count('b'))

#change elemente in list -elementul cu indexul 1 contine o noua lista in care pot pune m multe valori daca vreau
lista_mea[1] = [10]
lista_mea[1:3] = ['da', 'nu']
#imi inlocuieste elementele din lista cu ce i-am dat eu sa inlocuiasca
print(lista_mea)

#loop list- parcurge lista si poti face operatii
for x in lista_mea:
    print(x)


#Dictionar-in Java se numeste mapxz:"
'''stocam perechi de valori
prima e cheia tot tipul, apoi e valoarea cheii. In cazul nostru masina este cheia, iar automat este valoarea
nu putem avea chei duble, cheile sunt unice, dar nu iti da eroare, doar nu o ia in considerare
putem avea o cheie cu m multe valori le facem de tip lista []'''

dict_gol = {}

dict_meu = {
    'masina': 'BMW',
    'automata': True,
    'culoare':'verde'
}
print(dict_meu)

#valoarea unei chei
valoare = dict_meu['masina']
print(valoare)
print(dict_meu.get('automata'))

#aflam toate cheile din dictionar
print(dict_meu.keys())

#aflam toate valorile din dictionar
print(dict_meu.values())

#adaugare elem noi-prima e cheia a doua valoarea
dict_meu['culoare'] = 'verde'
print(dict_meu)

#suprascriere
dict_meu['masina'] = 'dacia'
print(dict_meu)

#transf dict intr-o lista-dict items
a = dict_meu.items()
print(a)
print(type(a))
print(type(dict_meu))

#check if key in dict
if 'culoare' in dict_meu:
    print('avem culoarea' + dict_meu ['culoare'])
elif 'dacia' in dict_meu.values():
    print('avem dacia')


#remove items
dict_meu.pop('culoare')
print(dict_meu)

#copiere de dict prin 2 metode
dict_nou = dict_meu.copy()
dict_extra_nou = dict(dict_meu)
print(dict_nou)
print(dict_extra_nou)

#nested dict def dict in alt dict
dict_tau = {
    'copil1' : {
        'nume': 'natalia',
        'ani': 1
    },
    'copil2': {
         'nume': 'sofia',
         'ani': 2
    }
}
print(dict_tau)

#len se poate folosi si la dict

#tuple-cum il definesti asa ramane, nu se poate adauga, sterge. Dar putem adauga cu o lista

#set
#valori unice, nu putem folosi index, slicing, putem doar aduga sau sterge elemente. Se poate folosi len

my_set ={'masina', 'casa', 12}

#accesare valori
for x in my_set:
    print(x)

my_set.add(False)
print(my_set)

#stergere element
my_set.remove("casa")
print(my_set)

#stergere un element random
my_set.pop()
print(my_set)
my_set.discard(12)

#update- se adauga la set
set_nou = {1,2,3}
my_set.update(set_nou)
print(my_set)