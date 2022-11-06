'''funcția divmod ()
divmod() este o funcție încorporată
careturnează coeficientul și restul la împărțirea numărului a după număr b.
Este nevoie de două numere ca argumente a & b. Argumentul nu poate fi un număr complex.'''

print(divmod(5,2)) # prints (2,1)
print(divmod(13.5,2.5)) # prints (5.0, 1.0)
q,r = divmod(13.5,2.5)  # Assigns q=quotient & r= remainder
print(q) # prints 5.0 because math.floor(13.5/2.5) = 5.0
print(r) # prints 1.0 because (13.5 % 2.5) = 1.0