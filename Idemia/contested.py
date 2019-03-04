class map():
    abj = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, x):
        self.x = x
        self.coo = []
        self.arm = 0

    def mat(self):
        arm = []
        coo = []
        for _ in range(len(self.x)): 
            for q in range(len(self.x[_])):
                if (self.x[_][q]) in map.abj:
                    self.arm.append(self.x[_][q])
                    self.coo.append([q, _])

    def pos(self):
        

x = ['###########....',
     '#.......c.###..',
     '####......#.#..', 
     '.#.########.#..',
     '##...#..b#..#..',
     '#.a.#...#...###',
     '####.#.#d###..#',
     '......#...e#xx#',
     '.#....#########',
     '.#.x..#..#.....',
     '.######.c#.....',
     '......####.....']
#x = ['.#', '#a']
"""
x = ['.s#q#####..#.#..',
'd##y..sua#.##..#',
'###h#..x#.......',
'##..#.##.....##.',
'.#.mb#n#..##..#.',
'..#.lr#..#.#..#.',
'..#.o.#..#.#...#',
'.#####...#.....#',
'#h#......#..#.##',
'.##..##..###.#.#',
'....#...#.......',
'...##...##.#.##.',
'..#qu##.....##.#',
'..##.#o##.#....#',
'...###p#..##..#.',
'..#.l.#...#n#.#.',
'...#y.#.#..#..#.',
'#..###...###....',
'..#.#..#.#.....#']
"""
mapc = map(x)
mapc.hor()
#mapc.conts()
#mapc.res()

"""
f = open('inputc.txt','r')
j = []
w = []
for _ in f:
    _ = _.replace('\n','')
    t = _.isdigit()
    if t != True: 
        j.append(_)
    else:
        if j != []:
            w.append(j)
            j = []
for x in w:
    print("Case " + str(w.index(x)+1) + ":")
    mapc = map(x)
    mapc.rep()
    mapc.conts()
    mapc.res()
"""