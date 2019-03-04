class t_all:
    def __init__(self, tx1, tx2, xcount):
        self.tx1 = tx1
        self.tx2 = tx2
        self.xcount = xcount

    def diamond(self):
        for _ in range(self.xcount):
            print ((self.tx1 * (1+(2*_))).center((x*2)-1))

        for _ in reversed(range(x)):
            print ((self.tx2 * (1+(2*_))).center((x*2)-1))

    def parallelogram(self):
        for _ in range(self.xcount):
            print ((self.tx1 * (1+(2*_))).center((x*2)-1))

        for _ in reversed(range(x)):
            print ((self.tx2 * (1+(2*_))).center((x*2)-1))

    def frm(self, c):
        return {
            1: self.diamond(),
            2: self.parallelogram()
        }[c]

x = int(input("Please Input x count value (1 - n), default(1) : ") or "1")
tx1 = input("Please Input text 1, default('0') : ") or "0"
tx2 = input("Please Input text 2, default('1') : ") or "1"

txt_all = t_all(tx1, tx2, x)

frm = int(input("Please choose the from (1. diamond, 2. parallelogram), default(1) : ") or "1")

txt_all.frm(frm)

