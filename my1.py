#time and threading modules
import threading
import time

def q ():
   for i in range (150):
       j=i
       if j >=0:
    
        print("yes")
        time.sleep(0)
t1=threading.Thread(target=q)
t1.start()


