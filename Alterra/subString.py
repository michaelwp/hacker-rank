def substringCalculator(s):
    r = []
    for _ in range(len(s)):
        for a in range(len(s)):
            x = s[_:len(s)-a]
            if x == '' or x in r:
               continue
            r.append(x)

    return(len(r))

print(substringCalculator('kincenvizh'));