print(min(2, 3)) # Returns 2 as 2 is the smallest of the two values
print(min(2, 3, -1)) # Returns -1 as -1 is the smallest of the two values

list1 = [1, 2, 4, 5, -54]
print(min(list1)) # Returns -54 as -54 is the smallest value in the list

list2 = ['a', 'b', 'c' ]
print(min(list2)) # Returns 'a' as 'a' is the smallest in the list in alphabetical order

list3 = [1, 2, 'abc', 'xyz']
print(min(list3)) # Gives TypeError as values in the list are of different type

#Fix the TypeError mentioned above first before moving on to next step

list4 = []
print(min(list4)) # Gives ValueError as the argument is empty