
#To get the number of thread objects currently alive

import threading as th
import time as t

def func(n):
    for _ in range(n) :
        print("Hi")
        t.sleep(1) 

x= th.Thread(target=func,args=(5,))
x.start()

print(th.active_count())

#To print active count at the end use join() method

