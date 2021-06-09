

#Program to print hello and hai alternatively using python


import threading as th
import time as t

def hello(n):
    for _ in range(n) :
        print("Hello")
        t.sleep(1)
def hi(n) :
    for _ in range(n) :
        print('Hi')
        t.sleep(1)

x=th.Thread(target=hello,args=(5,))
x.start()
y=th.Thread(target=hi,args=(5,))
y.start()

x.join()
y.join()

print("Done")