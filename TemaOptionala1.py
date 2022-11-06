'''ex 11
citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc'''
echipa = input('Barcelona')
mijloc = len('echipa') //2
print(mijloc)

'''ex 12 Folosind assert, verificati daca un string este palindrom'''
a = 'mare'
assert a == a[::-1]
print('Este palindrom.')

''' ex 13.
folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pentru verificare'''
a=input('Culorile preferate sunt')
b,c=a.split()
print(b)
print(c)

prenume ='Alexandra'
print(prenume)
nume = 'Delureanu'
print(nume)

''' ex 14. 
citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) 
capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
=> alAbAlA portocAla'''
text = input("Dati un text :")
primul_caracter = text[0]
text_truncat = text[1:-1]
text_modificat_partial= text_truncat.replace(primul_caracter, primul_caracter.capitalize())
text_modificat = text[0] + text[1:-1].replace(primul_caracter,primul_caracter.capitalize()) + text[0]
print(text)
print(text_modificat)


'''ex 15.
citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ****'''
user =input('user:')
parola =input('parola:')
print('Parola pt user' + str(user) +  'este'  + parola.replace(parola,'*') *len (parola) + 'si are' +  str(len(parola)) + 'caractere')







