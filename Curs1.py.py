#acesta este un comentariu
'''acesta este un
comentariu multiplu'''

#variabila este case sensitive
#trebuie sa folosim _ nu putem pune pauza
#tipuri de date
aceastaEsteVariabila = 'variabila'
#ex de mai sus este un string-sir de caractere

variabila_int = 10
#ex de mai sus este integer

variabila_float = 10.10
#ex de mai sus este float pt ca am pus si . la zecimale

variabila_boolean = True
x, y, z = 1, 2, 3
print (y)
#ne va printa 2

x=y=z= 10
print (z)
#ne va printa 10 pt ca e o suprascriere

variabila_int = '10'
#se schimba tipul de date se initializeaza din nou

y ='string'
print (y)

#functia type() defineste tipul de date, iti arata ce variabila ai folosit,ce ai in cutie
print(type(variabila_boolean))

#functia int() transforma in integer dar interpreteaza siruri care se refera la cifre
# functia str() modifica orice tip de date in string
motor_masina = '2000'
a = int(motor_masina)
print (int(motor_masina))
print (type(motor_masina))

#functia bool()
automata = 'True'
automata = bool(automata)
print(type(automata))


#concatenare- doar ac tip de date, ex 2 string, dar nu un string si un integer
tip_masina = 'Lamborghini'
model_masina = 'Urus'
print(tip_masina +  model_masina)
capacitate = 3000
masina_mea = tip_masina + model_masina
masina_ta = tip_masina +  str(capacitate)
print(masina_ta)

#assert() returneaza mereu o valoare boolean true sau false si e imp sa fie ultima linie de cod din textul tau
#assert compara orice tipuri de date


#input() dupa ce dam print trebuie sa scriem numele masinii in Run si dam enter
nume_masina = input

#index() arata pozitia unui element dintr-o lista
c = 'Ana are mere'
print(c[2])
#printeaza litera a pt ca incepe de la 0 iar spatiile sunt caractere,deci numarate

#len() numara cate caractere sunt
print(len(c))
#slicing()

#upper
print(c.upper())
print(c.lower())

#count arata de cate ori apare un element intr-un sir

# printam un mesaj in consola
 # string
marca = "Samsung"
model = "Note"

# integer
an = 2021;

# double/float- nr zecimal
pret = 2299.99

# boolean se scriu cu initiala mare
nou = False

# char nu avem
clasa = "A"


print(f'Vand telefon {marca} {model}, an fabricatie {an} cu pretul de {pret} lei. Telefonul este nou {nou} si clasa {clasa}')

print(len(clasa))

for i in range(1,20,3):
    print(i)


x = 5
y = 2
z = x** y
print(z)
