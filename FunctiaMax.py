print(max(2, 3)) # Returns 3 as 3 is the largest of the two values
print(max(2, 3, 23)) # Returns 23 as 23 is the largest of all the values

list1 = [1, 2, 4, 5, 54]
print(max(list1)) # Returns 54 as 54 is the largest value in the list

list2 = ['a', 'b', 'c' ]
print(max(list2)) # Returns 'c' as 'c' is the largest in the list because c has ascii value larger then 'a' ,'b'.

list3 = [1, 2, 'abc', 'xyz']
print(max(list3)) # Gives TypeError as values in the list are of different type