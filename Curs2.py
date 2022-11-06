# assert verifica un statatement, returneaza mereu un boolean true sau false
# assert not-se verifica negatia statementului si il lasa sa treaca mai departe

# operatori de atribuire
# atribuire simpla
x = 10
# adauga 5 la val lui x
x += 5
# scade 7 la val lui x
x -= 7
x *= 2
# restul impartirii de ex 9 impartit la 4 o sa imi afiseze 1-modulus
x %= 4
# impartire
x /= 3
# exponential spre ex x la puterea a doua
x //= 2

# operatori aritmetici
# exponential
x = 5
y = 2
z = x ** y
print(z)

# modulus
x = 5
y = 2
z = x % y
print(z)

# operatori de comparare
# egal
z == y
# diferit
x != y
# mai mare
x > y
# mai mic
x < y
# mai mare sau egal, mai mic sau egal
x >= y
x <= y

# operatori logici
# si- ambele tb sa indepl condt simultan altfel rez este false
x and y
# ori
x or y
# negatie transf in false daca e true si invers
not x

# if statement
# if avem 3 usi punem if+ statement si intram pe usa corecta
# se folosesc 4 spatii inainte de print
a = 20
b = 30
if b > a:
    print("succes")
if b > a and b == a:
    print("succes")
# indentare conteaza orice spatiu

#if else statement este o evaluare, evalueaza un statement
a = 20
b = 30
if (b + a) == 50 and b > a:
    print('succes')
else:
    print("mai incearca")

#if elseif statement
#ii punem mai multe condt, daca primele 2 nu trec merge mai departe, elif este un al doilea if, else e portita de iesire mereu
#intra pe prima care e true si iese,nu mai executa urmatoarele linii
a = 5
b = 9
if b < a:
    print('succes') #ne da false si merge la urm ramura e dif de else pt ca merge mai departe chiar daca prima condt e falsa
elif b > a:
    print("aici e bine")
elif a < b:
    c = a+b
    print(type(c))
else:
    print("iesire")

#if else is oneline- practic este o prescurtare a if-ului

#nested if- se evalueaza o expr dc e corecta, intra in ramura if si tb sa evalueze inca o expr cu if,dar ajunge la ultimul else daca primul if e fals
if a < b:
    if a+b == 15:
        print("succes3")
    else:
        print("iesire1")
else:
    print("iesire2")

#pass statement- te lasa sa treci mai departe
if a>b:
    pass
elif b==a:
    print(a)
else:
    print(b)

