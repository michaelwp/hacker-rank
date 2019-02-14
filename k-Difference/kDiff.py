
def kDifference(a, k):
    x = list(set(a))
    y = []
    r = 0
    for _ in x:
        for a in x:
            if (_ != a):
                c, d = max(_, a), min(_, a)
                if [c, d] not in y:
                    y.append([c, d])
    for _ in y:
        if (_[0]-_[1])==k: r += 1
    return(r)
    
    
##test
#a = [5, 1, 5, 3, 4, 2]
a = [6, 2, 4, 6, 8, 10, 12]
k = 2
print(kDifference(a, k))