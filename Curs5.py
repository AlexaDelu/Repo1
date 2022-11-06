from Curs6 import Persoana

'''FUNCTII
O zona de cod cu o mica logica proprie, care poate fi folosita/refolosita (apelata) de oricate ori avem nevoie.
BLOC DE COD REUTILIZABIL'''

def prima_functie(): #declararea unei functii
    print('Aceasta este prima functie') #corpul functiei

prima_functie() #apelarea functie, se va executa bucata de cod

#argument= parametru
#parametrii sunt optionali, sunt ca niste variabile declarate, dar neinitializate

#FUNCTII CU PARAMETRII
# #declaram niste variabile/1 variabila
def functie_cu_parametrii(a):
    print(f'parametrul este {a}')

functie_cu_parametrii(5)
functie_cu_parametrii([1,5,6])
functie_cu_parametrii(2)
functie_cu_parametrii('curs5')

def func_cu_2_params(a, b):
    print(f'suma este {a+b}')

func_cu_2_params(2, 5)

'''nu putem aduna string cu integer cum am avea mai jos
func_cu_2_params("2", 5)'''

#functie cu multiplii parametri
#se foloseste un key word-steluta- ca sa stie ca poate folosi oricati parametri, ajunge de genul unui tuple,numar indefinit
def func_cu_params_multiplii(*p):
    print(f'unul din parametrii este {p[1]}')

func_cu_params_multiplii(2,4,6, "param")
#se va printa parametrul 1, in cazul nostru 4

def functie_speciala(*masina):
#def o fct cu nr infinit de param si apoi parcurgem tuplel-ul
    for i in masina:
        if i == "bmw":
            print(f'o vreau eu {i}')

functie_speciala('dacia',  'opel',  'bmw')

#functie cu parametrii pasati ca si dictionar
#nr indefinit de parametrii
#dif este ca tb sa declaram parametrii
def functie_dict(**persoane):
    print(f'first name is: {persoane["prenume"]}')
    print(f'last name is: {persoane["nume"]}')

functie_dict(nume='serban', prenume='tibi')
#nume e cheia, prenume e cheia, tb sa definim mereu cheie-valoare, cheie-valoare


#functie cu param default
def func_param_default(a, b = 10):
    print(f'suma este: {a+b}')

#in cazul nostru tb sa definim doar 1 param ca celalalt este deja definit de sus
#dc sctiem 2 suprascrie param b
func_param_default(3)

#functie cu parametrii de tip lista

def func_lista(lista): #parametrul care tb pasat la apelare este o lista altfel nu merge, corpul fiind o functie
    for i in lista:
        print (i)

func_lista([1,4,7,9]) #am pasat o lista ca parametru

#daca nu dam print nu vedem ce se intampla


# functii cu RETURN- va returna mereu o valoare
def functie_return(a, b):
    return a+b  #aceasta functie va returna mereu o valoare

print(functie_return(10,12)) #se va printa ce va returna functia


#in cazul lui if else putem avea mai multe return, returneaza mai multe val in fct de ce parametrii ii dam.

def func_retur(x, y):
    if x>y:
        return x
    else:
        return y

print(func_retur(4,6))

# nu poti crea o fct sa returneze 2 valori gen return x+y, nu mai ia in considerare ce urmeaza dupa
'''def func_retur(x, y):
    if x>y:
        return x
    else:
        return y
return x+y #nu  se va ajunge'''


#VARIABILE LOCALE SI GLOBALE
a = 10 #variabila globala, poate fi folosita si in afara corpului fct
def func_var(b):  #b este parametru
    c = 15
    return a+b+c

print (c) #variabila  locala, poate fi folosita doar in int fct, da eroare
#putem da print doar (a)
print(func_var(4))


'''Scrie un program care sa afiseze numarul maxim dintre doua numere aleatoare.
Solutia pentru aceasta problema este urmatoarea:'''

 def valoareaMaxima( x, y ):
    if x > y:
        print(x)
    else:
        print(y)
valoareaMaxima(31, 7)