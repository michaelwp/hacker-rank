def dev(A, B, K):
    i = 0
    x = A
    while x <= B:
        if (x % K == 0):
            i += 1
        x += 1
    return str(i)

f = open("input.txt", "r")
line = f.readlines()
n = []
for _ in line:
    x = _.replace('\n','')
    n.append(x)

a = []
b = []
for _ in range(0, len(n), 3):
    b = (n[_], n[_+1], n[_+2])
    a.append(b)

i = 0
for _ in a:
    i += 1
    a = int(_[0])
    b = int(_[1])
    k = int(_[2])
    print("Case " + str(i) + ": " + (dev(a, b, k)))