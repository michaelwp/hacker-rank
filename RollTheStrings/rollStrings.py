def rollTheString(s, roll):
    ab = 'abcdefghijklmnopqrstuvwxyz'
    r = ''
    abi = 0
    x = ''
    for i in roll:
        for j in range(int(i)):
            abi = (ab.index(s[j])+1)
            if abi > 25:
                abi = 0
            r += (ab[abi])

        for _ in range(int(i), len(s)):
            x += s[_]

        s = (r + x)
        r = ''
        x = ''

    return(s)

## test
s = 'vwxyz'
roll = '12345'
print(rollTheString(s, roll))