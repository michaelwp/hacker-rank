def getTotalX(a, b):
    factor = []
    for n in range(a[len(a) - 1], b[0] + 1):
        factor.append(n)

    result = []
    for i in factor:
        isfactor = True
        for j in a + b:
            f = [i, j]
            f.sort()
            if f[1] % f[0] != 0:
                isfactor = False

        if isfactor:
            result.append(i)

    return len(list(dict.fromkeys(result)))


a = [2, 6]
b = [24, 36]

print(getTotalX(a, b))
