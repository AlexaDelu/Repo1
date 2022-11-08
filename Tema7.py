'''1.Git setup

OBLIGATORIU!
Creati-va cont de github si incarcati intr-un repo nou tot ce am facut pana acum la ore
Curs git/github
https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3'''

#2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)

from abc import abstractmethod
from abc import ABC


'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi'''

class FormaGeometrica():
    def __init__(self, aria):
        self.aria=aria
        self.pi= 3.14
    @abstractmethod
    def aria(self):
       raise

    def descrie(self):
        print (f'Cel mai probabil am colturi')


'''INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)'''


class Patrat(FormaGeometrica):
    # constructor
    def __init__(self, latura):
        self.latura= '15'

    @property  # initializam proprietatea variabilei private prin adnotare
    def latura(self):
        return self.__latura

    @latura.getter  # adnotare pt a seta valoare variabilei private
    def latura(self):
        return self.__latura

    @latura.setter  # adnotare pt a afla valoarea var private
    def latura(self, latura):
        self.__latura = latura
        print(f'latura este {self.__latura}')
a = Patrat('15')
a.latura

'''Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)'''

class Cerc(FormaGeometrica):
    # constructor
    def __init__(self, raza):
        self.raza= '100'

    @property  # initializam proprietatea variabilei private prin adnotare
    def raza(self):
        return self.__raza

    @raza.getter  # adnotare pt a seta valoare variabilei private
    def raza(self):
        return self.__raza

    @raza.setter  # adnotare pt a afla valoarea var private
    def raza(self, raza):
        self.__raza = raza
        print(f'raza este {self.__raza}')
a = Cerc('100')
a.raza


'''POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui

3. Actualizati proiectul pe github facand un push la noul cod
In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public

Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4'''
