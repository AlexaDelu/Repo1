#variabila este o cutie goala in care punem date

# string
marca = "Samsung"
model = "Note"
print(marca)

# integer
an = 2021;
print(an)

# float
pret = 2299.99
print(pret)

# boolean
nou = False
print(nou)

print(type(marca))
print(type(pret))
print(type(an))
print(type(nou))


# rotunjire float
pret = 2299.99
rounded_number = round(pret)
print(rounded_number)
print(type(rounded_number))

print(f'Vand telefon {marca} {model}')
print(f'Telefonul are anul de fabricatie {an}')
print(f'Pretul telefonului este {pret} lei')
print(f'Telefonul este nou {nou}')

name =input('name')
first_name =input('first_name')
print(name  + first_name)
print(len(name+ first_name))

Lungimea =input('lungime')
latimea =input('latimea')
aria = int(Lungimea) * int(latimea)
print(aria)

a ='Coral is the stupidest animal or the smartest rock'
print(a.count('the'))

original = 'Coral is the stupidest animal or the smartest rock'
replace = original.replace('the', 'THE')
print(replace)


