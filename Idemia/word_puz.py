class wd_matrix():
    def __init__(self, w, t):
        self.w = w
        self.t = t
        self.tr = ''.join(reversed(t))
        self.lt = len(t)
        self.lw = len(w[0])
        self.lwx = len(w)
        self.lc = self.lw - self.lt
        self.lr = self.lwx - self.lt

    def wcount(self, wc):
        return(wc.count(self.t) + wc.count(self.tr))
    
    def puz_hor(self):
        x = ""
        wx = []

        for s in self.w: 
            for _ in range((len(s)-self.lt)+1):
                for j in range(self.lt):
                    x += (s[_+j])
                wx.append(x)
                x = "" 
        return self.wcount(wx)

    def puz_ver(self):
        x = ""
        wx = []

        for s in range(self.lr + 1): 
            for _ in range(self.lw):
                for j in range(self.lt):
                    x += (self.w[s+j][_])
                wx.append(x)
                x = ""
        return self.wcount(wx)

    def puz_dig(self):
        x = ""
        y = ""
        wx = []
        z = []

        for _ in range(len(self.w)):
            z.append(self.w[_][::-1])

        for s in range(self.lr + 1): 
            for _ in range(self.lc + 1):
                for j in range(self.lt):
                    x += (self.w[s+j][_+j])
                    y += (z[s+j][_+j])
                wx.append(x)
                wx.append(y) 
                x = ""
                y = ""
        return self.wcount(wx)

f = open('input_puz.txt','r')
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
x = []
i = 0
for _ in w:
    i += 1
    x = _[:-1]
    t = _[-1]
    wmatrix = wd_matrix(x, t)
    print("Case " + str(i) + ": " + str(wmatrix.puz_hor() + wmatrix.puz_ver() + wmatrix.puz_dig()))