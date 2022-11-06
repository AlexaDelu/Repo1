#funcția len ()
#len() este o funcție încorporată
# Această metodă returnează lungimea (numărul de articole) al unui obiect. Este nevoie de un argument x.

'''Argumente
Este nevoie de un argument, x. Acest argument poate fi o secvență (cum ar fi un șir, octeți, tupluri, liste sau intervale) sau o colecție (cum ar fi un dicționar, un set sau un set înghețat).

Valoare returnată
Această funcție returnează numărul de elemente din argument care este transmis la len() funcţie.'''

#Exemplu de cod
list1 = [123, 'xyz', 'zara'] # list
print(len(list1)) # prints 3 as there are 3 elements in the list1

str1 = 'basketball' # string
print(len(str1)) # prints 10 as the str1 is made of 10 characters

tuple1 = (2, 3, 4, 5) # tuple
print(len(tuple1)) # prints 4 as there are 4 elements in the tuple1

dict1 = {'name': 'John', 'age': 4, 'score': 45} # dictionary
print(len(dict1)) # prints 3 as there are 3 key and value pairs in the dict1