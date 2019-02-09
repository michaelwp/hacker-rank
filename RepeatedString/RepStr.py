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
<<<<<<< HEAD
# the result should be = 162401559918
=======
# the result should be = 162 401 559 918
>>>>>>> ec37d8786fb0bd5639d0a97c0599b0d1ab91b94d
print(repeatedString(s, n))



