def minimumBribes(q):
    r = 0
    for i, P in enumerate(q):
        if P - (i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, (P-2)), i+1):
            if q[j] > q[i]:
                r += 1
    print(r)

## test
#q = [[2, 1, 5, 3, 4], [2, 5, 1, 3, 4]]
q = [[5, 1, 2, 3, 7, 8, 6, 4], [1, 2, 5, 3, 7, 8, 6, 4]]
for _ in range (len(q)):
    minimumBribes(q[_])