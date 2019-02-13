def minimumSwaps(arr):
    r = 0
    _ = 0
    while _ < len(arr):
        if (_+1) == (arr[_]):
            _ += 1
            continue
        arr[arr[_]-1], arr[_] = arr[_], arr[arr[_]-1]
        r += 1
    return(r)

## test
arr = [2, 3, 4, 1, 5]
#arr = [4, 3, 1, 2]
#arr = [1, 3, 5, 2, 4, 6, 7]
print(minimumSwaps(arr))
#minimumSwaps(arr)