def equalizeArray(arr):
    arr = arr.split(' ')
    x = {}
    for _ in arr:
        x[_] = arr.count(_)
    
    y = []
    for _ in x:
       y.append(x[_])
    r = 0

    mz = min(y)
    my = max(y)

    cy = (y.count(my)-1)*my

    if mz != my:
        for _ in y:
            if _ != my:
               r += _
        return(r + cy)
    else:
        return(sum(y) - mz)
        


## Test
# arr = '3 3 2 1 3'
#arr = '1 2 3 1 2 3 3 3'
#arr = '37 32 97 35 76 62'
arr = '10 27 9 10 100 38 30 32 45 29 27 29 32 38 32 38 14 38 29 30 63 29 63 91 54 10 63'
#arr = '24 29 70 43 12 27 29 24 41 12 41 43 24 70 24 100 41 43 43 100 29 70 100 43 41 27 70 70 59 41 24 24 29 43 24 27 70 24 27 70 24 70 27 24 43 27 100 41 12 70 43 70 62 12 59 29 62 41 100 43 43 59 59 70 12 27 43 43 27 27 27 24 43 43 62 43 70 29'
print(equalizeArray(arr))