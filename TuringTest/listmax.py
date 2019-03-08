class GetListMax:
    @staticmethod
    def listMax(n, operations):
        #Please write your code here.
        x = []
        for _ in range(n):
            x.append(0)

        for _ in operations:
            for q in range(len(_)-1):
                x[_[q]-1] += _[-1]
        return(max(x))
        return None


n = 5
operations = [[1, 2, 100],[2, 5, 100], [3, 4, 100]]
print(GetListMax.listMax(n, operations))