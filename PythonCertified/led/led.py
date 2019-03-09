from termcolor import colored

def leds(n=0):
    led = [ ('###','# #','# #','# #','###'),
            ('  #','  #','  #','  #','  #'),
            ('###','  #','###','#  ','###'),
            ('###','  #','###','  #','###'),
            ('# #','# #','###','  #','  #'),
            ('###','#  ','###','  #','###'),
            ('###','#  ','###','# #','###'),
            ('###','  #','  #','  #','  #'),
            ('###','# #','###','# #','###'),
            ('###','# #','###','  #','###')]
    #print('\n') ## whitespace
    for _ in range(5):
        for s in n:
            print (colored(led[int(s)][_], color='green'), end=' ')
        print('')

def ledq():
    try:
        x = (input(colored("Input number (>= 0), default (0) : ",color="yellow"))) or 0
        assert int(x) >= 0
        q = list(str(x))
        leds(q)
    except ValueError:
        print(colored("The Number you entered is Invalid\n", color="red"))
        ledq()
    except AssertionError:
        print(colored("The Number must >= 0\n","lightred"))
        ledq()

if __name__ == "__main__":
    print('\n') ## whitespace
    ledq()
    print('\n') ## whitespace