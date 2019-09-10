def birthday(s, d, m):
    x = 0
    r = len(s)-(m-1)

    for _ in range(r):
        if (sum(s[_:m+_])) == d :
            x += 1
    return x


d = 18
s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
m = 7
print (birthday(s, d, m))