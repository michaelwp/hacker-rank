def pallindrome(str):
    x = 0
    a = []
    for _ in range(len(str),0,-1):
        for j in range(len(str), 0, -1):
            if str[x:j] == str[x:j][::-1]:
                return (str[x:j][::-1])
        x += 1

print(pallindrome("babad"))