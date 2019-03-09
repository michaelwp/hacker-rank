def readint(prompt, min, max):
    try:
        x = int(input(prompt))
        assert x >= min and x <= max
        return x
    except AssertionError:
        print("Error: the value is not within permitted range (min..max)")
        q()

def q():
    try:
        v = readint("Enter a number from -10 to 10: ", -10, 10)
        assert v != None
        print("The number is:", v)
    except ValueError:
        print("Error: wrong input")
        q()
    except AssertionError:
        return

if __name__ == "__main__" :
    q()