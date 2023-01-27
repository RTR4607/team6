from threading import *
import time
l=Semaphore(2)
def wish(name):
    l.acquire()
    for i in range(10):
        #print("hello")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args={'tiru'})
t2=Thread(target=wish,args={'thiru'})
t3=Thread(target=wish,args={'tiruu'})
t4=Thread(target=wish,args={'thiruu'})
t1.start()
#t1.join()
t2.start()
t3.start()
t4.start()