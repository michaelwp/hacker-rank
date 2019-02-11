def rotLeft(a, d):
    r = []
    for _ in range(len(a)):
        x = (_ + d)
        if x >= len(a): x = x - len(a)
        r.append(a[x])
    return(r)

## test
a = [1, 2, 3, 4, 5] 
d = 4
print(rotLeft(a, d))