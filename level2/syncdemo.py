from threading import *
import time
def wish(name):
    for i in range(10):
        print("hello",end='')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args={'tiru'})
t2=Thread(target=wish,args={'thiru'})
t1.start()
t1.join()
t2.start()