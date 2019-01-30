def rollTheString(s, roll):
    ab = 'abcdefghijklmnopqrstuvwxyz'
    r = ''
    abi = 0
    sN = []
    x = ''
    for i in roll:
        for j in range(int(i)):
            abi = (ab.index(s[j])+1)
            if abi > 25:
                abi = 0
            r += (ab[abi])

        for _ in range(int(i), len(s)):
            x += s[_]

        sN.append(r + x)
        s = (r + x)
        r = ''
        x = ''

    return(sN)

## test
s = 'abz'
roll = '3'
print(rollTheString(s, roll))