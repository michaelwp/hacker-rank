def jumpingOnClouds(c):
    ct = 0
    jm = 0
    c.append(1)
    for _ in range( len(c)):
        if c[_] == 0:
            ct += 1
        else:
            jm += (ct//2)+1
            ct = 0
    return(jm-1)

## Test
c = [0, 0, 0, 0, 1, 0, 0]
# c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))