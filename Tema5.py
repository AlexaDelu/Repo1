import math

'''a. Usor (recomandat)
1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine. 
https://www.itfactory.ro/8174437-intro-in-programare/

Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul

b. Dificultate: usor spre mediu '''

#1. Functie care sa calculeze si sa returneze suma a 2 numere
def func_suma (a,b):
  return a+b

print(func_suma(12,65))

def func_cu_2_numere (a, b):
    print(f'suma este {a+b}')

func_cu_2_numere(7, 9)

#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def func_retur(numar):
    if numar%2==0:
        return 'true'
    else:
        return 'false'
x =func_retur (54)
print('Este:',x)

'''3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu)'''
def lungime(nume):
    a = len(nume) - nume.count(" ")
    return a
b= lungime('Delureanu Anamaria Alexandra')
print('Numarul total de caractere este', b)

#sau
'''def nr_char(nume):
    nume = nume.re'''

#4. Functie care returneaza aria dreptunghiului
def aria_dreptunghi(L,l):
    aria=L*l
    return aria
x=aria_dreptunghi(4, 7)
print(x)


#5. Functie care returneaza aria cercului
def aria_cerc(r):
    aria=math.pi*r**2
    return aria
x=aria_cerc(4)
print(x)

'''6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu'''
def functie_speciala(a,caractere):
    for i in range(len(caractere)):
        if a == caractere[i]:
            return True
            return False
x= functie_speciala('f','afara')
print(x)


'''7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y'''
def string_test(s):
  d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
  for i in s:
    if i.isupper():
      d["UPPER_CASE"] += 1
    elif i.islower():
      d["LOWER_CASE"] += 1
  print("Original String : ", s)
  print("No. of Upper case characters : ", d["UPPER_CASE"])
  print("No. of Lower case Characters : ", d["LOWER_CASE"])
string_test('Azi lucrez la tema')

#sau
def cauta(caracter):
    return caracter in STRING


#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def func_pozitiv(lista):
    lista_poz=[]
    for i in range(len(lista)):
        if lista[i]>=0:
            lista_poz.append(lista[i])
    return lista_poz
x=func_pozitiv([-34,-2,756,9234])
print('Lista cu numere pozitive este:', x)

'''9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. '''
def func_noreturn(a,b):
    if a>b:
       print('Primul numar',a, 'este mai mare decat al doilea numar', b)
    elif a<b :
        print('Al doilea numar', a, ' este mai mare decat primul numar', b)
    else:
        print('Numerele sunt egale')
func_noreturn(18745,543)


'''10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''
def func_add(x,y):
    if x not in y:
        y.add(x)
        print('Am adaugat numarul ', x, 'in setul', y)
        return True
    else:
        print('Nu am adaugat numarul', x, 'in setul', y, '.Acesta exista deja.')
        return False
a=func_add(2,{10,100,1000})
print('Valoarea afirmatiei este', a)


