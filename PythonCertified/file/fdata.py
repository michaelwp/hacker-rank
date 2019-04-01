class sdata():
    def __init__(self, data, fname):
        self.fn = [_[0] for _ in data]
        self.ln = [_[1] for _ in data]
        self.sp = [_[2] for _ in data]
        self.fname = fname
        self.__idata()
        self.__rdata()

    def __idata(self):
        fopen = open(self.fname, 'wt')
        for _ in range(len(self.fn)):
            fopen.write(self.fn[_] + '\t' + self.ln[_] + '\t' + str(self.sp[_]) + '\n')
        fopen.close

    def __rdata(self):
        dTxt = []
        r = {}
        with open(self.fname, 'rt') as fread:
            x = str(fread.read())
        
        for _ in x.split('\n'):
            if _ != '':
                dTxt.append(_)

        for _ in range(len(dTxt)):
            dTxt[_] = dTxt[_].split('\t')
            dTxt[_] = [(dTxt[_][0] + ' ' + dTxt[_][1]), float(dTxt[_][2])]

        dTxt.sort()

        for _ in dTxt:
            r[_[0]] = 0
        
        for _ in r:
            for q in dTxt:
                if q[0] ==  _:
                    r[_] += q[1]
            print(_, r[_])
    


dt = [['John','Smith',5],
      ['Anna','Boleyn',4.5],
      ['John','Smith',2],
      ['Anna','Boleyn',11],
      ['Andrew','Cox',1.5]]

fname = input('Input file name : ')
      
sd = sdata(dt, fname)
sd.__idata()