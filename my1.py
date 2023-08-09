#time and threading modules
import threading
import time
j= [range(100)]
def q ():
    while global j<=0:
        print("yes")
        time.sleep(1)
t1=threading.Threads(target=q,demon=true)
t1.start()

