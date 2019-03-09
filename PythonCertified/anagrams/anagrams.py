a = list((input('text 1 :')).lower())
b = list((input('text 2 :')).lower())
r = 'Anagrams'

for _ in b:
    if _ not in a:
        r = 'Not anagrams'
        break
print(r)