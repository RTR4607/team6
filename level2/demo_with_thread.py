from threading import *
import time
def double(num):
    for n in num:
        time.sleep(2)
        print(2*n)
def square(num):
    for n in num:
        time.sleep(2)
        print(n*n)
n=[1,2,3,4,5]
b=time.time()
t1=Thread(target=double,args=(n,))
t2=Thread(target=square,args=(n,))
t1.start()
t1.join()# is used to one process is completed after that second process will start
t2.start()
e=time.time()
print(e-b)
