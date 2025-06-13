import time
from threading import Thread

def main():
    t = Thread(target=cust_one)
    t.run()
#    while (1==1):
#        print(time.monotonic())
#        time.sleep(0.9)
#        while (time.monotonic() % 1 > 0.01):
#            time.sleep(0.001)

def cust_one():
    print("thread safe")

if __name__ == '__main__':
    main()