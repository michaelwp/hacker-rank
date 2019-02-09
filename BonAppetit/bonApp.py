def bonAppetit(bill, k, b):
    blx = 0
    for _ in bill:
        blx += _

    an = ((blx - bill[k])/2)
    r = (b - an)

    if r > 0:
        print(round(r))
    else:
        print('Bon Appetit')


## test
bill = [3, 10, 2, 9]
k = 1
b = 12
bonAppetit(bill, k, b)