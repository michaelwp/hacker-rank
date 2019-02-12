import random
def catAndMouse(x, y, z):
    a = abs(z - x)
    b = abs(z - y)
    if a < b :
        return('Cat A')
    elif b < a:
        return('Cat B')
    elif a == b:
        return('Mouse C')

##test
q = random.randint(1, 100)
for _ in range(q):
    x, y, z = random.randint(1,100), random.randint(1,100), random.randint(1,100)
    print(catAndMouse(x, y, z))