#import math
def pageCount(n, p):
    px = round(p /2)
    nx = round(n /2)
    rx = (nx - px)
    return(min(px, rx))

## test
n = 37455
p = 29835
print(pageCount(n, p))