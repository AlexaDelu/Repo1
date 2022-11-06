'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’'''

class FormaGeometrica

    class Factura():
        seria = 'FPP'
#metode
        def __init__(self, numar, nume_produs, cantitate, pret_buc):
            self.numar = numar
            self.nume_produs = nume_produs
            self.cantitate = cantitate
            self.pret_buc = pret_buc

'''1.Git setup

OBLIGATORIU!
Creati-va cont de github si incarcati intr-un repo nou tot ce am facut pana acum la ore
Curs git/github
https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3

2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)

ABSTRACTION 
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)

Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)

POLYMORPHISM 
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’


Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui

3. Actualizati proiectul pe github facand un push la noul cod
In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public

Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4'''

