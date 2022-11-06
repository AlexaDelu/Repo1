'''b. Usor spre Mediu (obligatoriu)
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte. 
X este un int'''

'''1.Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
if else statement este o evaluare, evalueaza un statement
if else e o declarație condițională care execută un bloc de cod când o anumită condiție a fost îndeplinită'''

#2.Verifica si afiseaza daca x este numar natural sau nu
x = int(input('x este:'))
if x > 0:
    print('x este numar natural')
else:
    print('x nu este numar natural')

#3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutrux = -5000
x = int(input('x este:'))
if x>0:
    print('X este numar pozitiv')
elif x==0:
    print('X este numar neutru')
elif x<0:
    print('X este numar negativ')

#4.Verifica si afiseaza daca x este intre -2 si 13
x =5
if x > -2 and x < 13:
    print("X este intre -2 si 13")
else:
    print("X nu este intre -2 si 13")

#5.Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = 7
y = 6
if (x-y) < 5:
    print('Diferenta dintre x si y este mai mica de 5')
else:
    print('Diferenta dintre x si y nu este mai mica de 5')

#6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
x = int(input('x este:'))
if not( 5 < x < 27):
    print('x NU este intre 5 si 27')
else:
  print('x este intre 5 si 27')

#7.x si y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
x = int(input('x este:'))
y = int(input('y este:'))
if x == y:
    print('X si y sunt egale')
elif x>y:
    print(x)
elif y>x:
    print(y)

'''8. X, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.'''
x = int(input('x este:'))
y = int(input('y este:'))
z = int(input('z este:'))
if x == y == y== z:
    print('Triunghiul este echilateral')
elif x!=y!=z:
    print('Triunghiul este oarecare')
else:
    print('Triunghiul este isoscel')

'''9. Citeste o litera de la tastatura
Verifica si afiseaza daca este vocala sau nu'''
litera = input('litera este:')
if litera.lower() in ('a','e','i','o','u'):
    print('Litera este vocala')
elif litera.upper() in ('A', 'E', 'I', 'O','U'):
    print('Litera este vocala')
else:
    print('Litera nu este vocala')


'''10.
Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''

nota = int(2.50)
if nota >= 9:
    print ('Nota este A')
elif nota >= 8:
    print('Nota este B')
elif nota >= 7:
    print('Nota este c')
elif nota >= 6:
    print('Nota este D')
elif nota > 4:
    print('Nota este E')
else nota <= 4:
    print('Nota este F')


