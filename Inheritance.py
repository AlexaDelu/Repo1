#conceptul care da voie unei clase sa preia prop altei clase


class Persoana:
    nume = "Tibi" #acesta este un atribut, nume este o variabila locala din int acestei clase, nu poate fi modif,doar accesat
    sex  = 'M'
    inaltime = '1.9'

class Atlet(Persoana):
    viteza = '12m/s'

class Angajat(Persoana):
    functie = 'programator'

persoana3 =Angajat
print(persoana3.nume)

#POLIMORFISM
#creeam m multe copii ale ac metode
#ex:in cosul cu frcute putem crea mai multe obiecte de anumite tip cu caract diferite