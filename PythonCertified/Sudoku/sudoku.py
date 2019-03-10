
class sudoku():
    b = []
    sud = 'Yes'
    def board(s):
        x = ''
        s = 'x' + s
        for _ in range(1,len(s)):
            x += s[_]
            if (_ % 9) == 0:
                sudoku.b.append(x)
                x = ''
        return(sudoku.b)

    def hor(b):
        for _ in b:
            for q in _:
                if _.count(q) > 1:
                    sudoku.sud = 'No'
                    break

    def ver(b):
        n = []
        j = ''
        for _ in range(len(b[0])):
            for x in range(len(b)):
                j += b[x][_]
            n.append(j)
            j =''
        sudoku.hor(n)

    def box(b):
        n = []
        j = ''
        for _ in range(0, len(b), 3):
            for x in range(0, len(b[0]), 3):
                for q in range(3):
                    for i in range(3):
                        j += (b[_+q][x+i])
                n.append(j)
                j = ''
        sudoku.hor(n)


#s = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"
s = "195743862431865927876192543387459216612387495549216738763524189928671354254938671"

sd = sudoku.board(s)
sudoku.hor(sd)
sudoku.ver(sd)
sudoku.box(sd)
print(sudoku.sud)