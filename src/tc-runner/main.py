import time
from threading import Thread
import random
from car import Car

def main():
#    t = Thread(target=cust_one)
#    t.run()
#    while (1==1):
#        print(time.monotonic())
#        time.sleep(0.9)
#        while (time.monotonic() % 1 > 0.01):
#            time.sleep(0.001)
    print("Welcome to the DMV. Take a number and a seat and we'll be right with you.")
    #num = random.randint(1,5)
    #print(num)
    c1 = Car(0, 180)
    print(c1)


#def cust_one():
#    print("thread safe")

if __name__ == '__main__':
    main()