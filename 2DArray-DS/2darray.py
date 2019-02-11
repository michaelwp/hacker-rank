def hourglassSum(arr):
    x = []
    y = []
    z = []
    r = []
    for _ in range(4):
        for a in range(4):
            x.append([arr[_][a], arr[_][a+1], arr[_][a+2]])
            y.append(arr[_+1][a+1])
            z.append([arr[_+2][a], arr[_+2][a+1], arr[_+2][a+2]])

    for a, b, c in zip(x, y, z):
         r.append(sum(a)+b+sum(c))

    mh = r.index(max(r))

    ## print the hourglass form, the highest sum will marked with red color
    print('\nThe hourglass form (the red mark is the highest sum of hourglass value):')
    for _ in range(4):
        n = 4 * (_+1)
        for _ in range((n-4), n):
            if _ == mh:
                print('\033[1;37;41m' + str(x[_][0]), x[_][1], x[_][2], end='\t')
            else:
                print('\033[0;37;40m' + str(x[_][0]), x[_][1], x[_][2], end='\t')
        print('')
        for _ in range((n-4), n):
            if _ == mh:
                print('\033[1;37;41m' + ' ', y[_], ' ', end='\t')
            else:
                print('\033[0;37;40m' + ' ', y[_], ' ', end='\t')
        print('')
        for _ in range((n-4), n):
            if _ == mh:
                print('\033[1;37;41m' + str(z[_][0]), z[_][1], z[_][2], end='\t')
            else:
                print('\033[0;37;40m' + str(z[_][0]), z[_][1], z[_][2], end='\t')
        print('\n')
    
    ## print the number of the largest hourglass sum
    print('\nthe largest (maximum) hourglass sum :', max(r))


        
## test
arr = [[1, 1, 1, 0, 0, 0], 
       [0, 1, 0, 0, 0, 0], 
       [1, 1, 1, 0, 0, 0], 
       [0, 0, 2, 4, 4, 0], 
       [0, 0, 0, 2, 0, 0], 
       [0, 0, 1, 2, 4, 0]]
hourglassSum(arr)