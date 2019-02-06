import math
def repeatedString(s, n):
    sl = len(s)
    sa = s.count('a')
    nx = math.floor(n/ sl)
    ny = n - (sl * nx)
    xa = (s[:ny].count('a'))
    a = (nx * sa) + xa 
    return(a)

## Test
s = 'bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc'
n = 649606239668
# the result should be = 162 401 559 918
print(repeatedString(s, n))



