def countingValleys(n, s):
    sN = [0]
    vN = []
    for _ in s:
        if _ == 'D':
            sN.append(-1)
        else:
            sN.append(1)

    x = sN[0]
    for _ in range(len(sN)-1):
        x += sN[_+1]
        vN.append(x)
    
    vP = 0
    for _ in range(len(vN)-1):
        if (vN[_] < 0) and (vN[_+1] == 0):
            vP += 1
    
    print(str(sN) + '\n' + str(vN))
    return(vP)


## test
n = 10
s = "DUDDDUUDUU"
print(countingValleys(n, s))