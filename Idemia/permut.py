def permutations():
    global running
    global characters
    global bitmask
    if len(running) == len(characters):
        a = (''.join(running))
        print(''.join(running))
        j.write(a + '\n')
    else:
        for i in xrange(len(characters)):
            if characters[i] not in running:
            #if ((bitmask>>i)&1) == 0:
                #bitmask |= 1 << i
                running.append(characters[i])
                permutations()
                running.pop()

x = []
f = open('testx.txt','r')
for _ in f:
    x.append(_.replace('\n', ''))

j = open('test.txt','w')

for _ in x:     
    raw = _ #raw_input()
    characters = list(raw)
    running = []
    bitmask = 0
    permutations()