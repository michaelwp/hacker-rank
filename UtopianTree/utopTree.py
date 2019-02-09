def utopianTree(n):
    x = 0
    for _ in range(n+1):
        if (x%2) == 0:
            x += 1
        else:
            x += x
    return(x)

## test
n = [4, 3]
for _ in range(len(n)):
    print(utopianTree(n[_]))
