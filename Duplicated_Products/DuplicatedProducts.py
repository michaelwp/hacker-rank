def numDuplicates(names, prices, weights): 
    x = []
    for i in range(len(names)):
        x.append(names[i]+str(prices[i])+str(weights[i]))

    res = {}
    d = 0
    r = 0
    for ye in x:
        for xe in x:
            if (xe == ye):
                d+=1
        if (d > 1):
            res[ye] = d
        d = 0

    for e in res:
        r = r + (res[e])

    return r

## Test
n = ['ball','ball','mango','coconut','mango','mango']
p = [1, 1, 2, 3, 2, 2]
w = [1, 1, 3, 2, 3, 3]
print(numDuplicates(n, p, w))