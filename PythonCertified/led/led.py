
def leds(n=0):
    led = [ ('###','# #','# #','# #','###'),
            ('  #','  #','  #','  #','  #'),
            ('###','  #','###','#  ','###'),
            ('###','  #','###','  #','###'),
            ('# #','# #','###','  #','  #'),
            ('###','#  ','###','  #','###'),
            ('###','#  ','###','# #','###'),
            ('###','  #','  #','#  ','  #'),
            ('###','# #','###','# #','###'),
            ('###','# #','###','  #','###')]
    
    for _ in range(5):
        for s in n:
            print(led[int(s)][_], end=' ')
        print('')

def ledq():
    try:
        n = (input("Input number (>= 0), default (0) : ")) or 0
        q = list(str(n))
        leds(q)
    except ValueError:
        print("The Number you entered is Invalid")
        ledq()

if __name__ == "__main__":
    ledq()