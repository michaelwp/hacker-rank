def getMoneySpent(keyboards, drives, b):
    r = []
    for rk in keyboards:
        for rd in drives:
            dk = (int(rd) + int(rk)) 
            if dk <= b:
                r.append(dk)
    if len(r) > 0:
        return(max(r))
    else:
       return(-1)


##test
k = [40, 50, 60]
d = [5, 8, 12] 
b = 60
print(getMoneySpent(k, d, b))