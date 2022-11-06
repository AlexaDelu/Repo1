#importam o clasa din alt fisier
#from folder.folder.fisier import nume_clasa
#from .....import ..... clasa

#CLASA
'''O clasa este o reteta (blueprint) pentru crearea obiectelor

Ea contine elemente descriptive: atribute/fields
(practic niste variabile)
Contine actiuni posibile: metode (practic niste functii)
Self - este instanta clasei, ajuta functia sa aiba acces
la  atributele/metodele clasei'''

#EX: 1 cos cu fructe e o clasa, marul din acel cos este un obiect, metode-sa aflam numarul fructelor din cos
#clasele e bn sa fie scrise cu majuscula, fct cu litera mica

class Persoana:
    nume = "Tibi" #acesta este un atribut, nume este o variabila locala din int acestei clase, nu poate fi modif,doar accesat
    sex  = 'M'
    inaltime = '1.9'

'''Obiect = instanta a clasei
Toate obiectele de tip Persoana vor avea acelasi comportament ,aceleasi atribute, aceleasi metode
Atributele pot suferi modificari dupa initializarea obiectului'''

#self este o ref a instantei curente din clasa,adica un obiect din clasa
#self e mereu primul parametru
    def prezentare(self): #fct locala din int clasei, poate fi doar accesata
        print(f'Ma numesc', self.nume, 'si am inaltimea', self.inaltime)


#def obiecte care pot fi modificate din afara
#init adauga val noi atributelor din clasa
    def __init__(self, nume, sex, inaltime):
        self.nume = nume
        self.sex = sex
        self.inaltime = inaltime
        self.varsta = varsta

#self este un keyword
#persoana1 este un obiect, orice variabila este un obiect

persoana1 = Persoana() #initializarea unui obiect
print(persoana1.nume) #folosirea unui atribut din clasa in obiectul definit
#apelam o metoda din clasa pers prin intermediul obiectului1
persoana1.prezentare()  #apelarea unei metode din clasa prin intermediul ob personal

persoana2 = Persoana ('Ovidiu', 'M', '1.84', '27')
print((persoana2.varsta))

#conceptul care da voie unei clase sa preia prop altei clase

#INHERITANCE
class Persoana:
    nume = "Tibi" #acesta este un atribut, nume este o variabila locala din int acestei clase, nu poate fi modif,doar accesat
    sex  = 'M'
    inaltime = '1.9'

class Atlet (Persoana): #mosteneste atribute si metode din clasa persoane,dr invers nu
    viteza = '12m/s'

class Angajat(Persoana):
    functie = 'programator'

persoana3 =Angajat
print(persoana3.nume) #putem accesa atribute din clasa mostenita

#Constructor
'''se asigura ca la crearea obiectelor setam niste date fara de care obiectul nu are sens sa existe
Practic atribuie valori atributelor
Daca ne gandim la un formular, ar fi acele field-uri cu *
care sunt obligatorii'''


class Vehicul:
    def __init__(self, cap_cilindrica, consum, numar_locuri):
        self.cap_cilindrica = cap_cilindrica
        self.consum = consum
        self.numar_locuri =numar_locuri

    def prezentare(self):
       print(f' Masina noastra este un vehicul cu capacitatea cilindrica {self.cap_cilindrica} si un numar de locuri {self.numar_locuri}')


class Masina(Vehicul):

    def __init__(self, model):
        self.model = model

vehicul = Vehicul ('2.0 TDI', '9', '5')
vehicul.prezentare()

masina = Masina('Dacia')
print(masina.model)

masina.consum = '6'
print(masina.consum)


class Cerc:
    pi = 3.14

    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return int(self.pi) * int (self.raza) **2

cerc = Cerc ('18')
print (cerc.aria())





