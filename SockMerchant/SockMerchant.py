def sockMerchant(n, ar):
    x = []
    r = 0;
    for _ in ar:
        t = ar.count(_)
        if (_ not in x) and (t > 1):
            x.append(_)
    
    for _ in x:
        d = ar.count(_)
        if (d % 2) != 0:
            d -= 1 
        r += d

    return(round(r/2))
         
#test case
n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

print(sockMerchant(n, arr))
