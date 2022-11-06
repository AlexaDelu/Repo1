s = 'supercalifragilisticexpialidocious'

print(s.count('p'))
# 2

c = collections.Counter(s)

print(c)
# Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})