n = int(input('Masukkan nilai n : '))
s = ' '
x = '1'
o = '0'

if n == 1: 
    print(1)
    pass

i = 1
xs = ''
j = 0    
while i <= (n-1):
    while j < (i):
        if j & 1: 
            xs += o
        else:
            xs += x
        print((s * (n-1)) + xs)
        j += 1
    i += 1

ys = ''
for _ in range((n*2)-1):
    if _ & 1:
        ys += o
    else: 
        ys += x
print(ys)

k = (n -1)
while k > 0:
    zs = ''
    for _ in range(k):
        if _ & 1:
            zs += o
        else:
            zs += x
    print((s * (n-k)) + zs)
    k-=1