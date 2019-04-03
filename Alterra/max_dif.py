def maxDifference(a):
    x = []
    for _ in range(len(a)):
        for n in range(_):
            if (a[_] > a[n]) and (a[n] < 0):
                x.append(a[_] + a[n])
            elif (a[_] > a[n]):
                x.append(a[_] - a[n])
            else:
                x.append(-1)

    return(max(x))

a = [10, 0, 9, 6, 5]
print(maxDifference(a))