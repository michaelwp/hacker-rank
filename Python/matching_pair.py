class matchPair():
    def __init__(self, arr):
        self.arr = arr

    def match(self):
        x = []
        r = 0;
        for _ in self.arr:
            t = self.arr.count(_)
            if (_ not in x) and (t > 1):
                x.append(_)
    
        for _ in x:
            d = self.arr.count(_)
            if (d % 2) != 0:
                d -= 1 
            r += d

        return(round(r/2))
        



#test case
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

mPair = matchPair(arr)
print(mPair.match())
