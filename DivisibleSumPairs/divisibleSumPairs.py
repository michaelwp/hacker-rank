def divisibleSumPairs(n, k, ar):
    res = 0

    if len(ar) == 2:
        if (ar[0] + ar[1]) % k == 0:
            res += 1
        return res
    else:
        for i in range(1, len(ar)):
            if (ar[0] + ar[i]) % k == 0:
                res += 1
        return res + divisibleSumPairs(n, k, ar[1:])


ns = 6
ks = 3
ars = [1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(ns, ks, ars))
