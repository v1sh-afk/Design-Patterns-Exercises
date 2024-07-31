import threading
import time
print(threading.active_count())
def print_thread(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "---------", time.time())
        print(threading.active_count())

if __name__=="__main__":

    '''class threading.Thread(group=None, target=None, name=None, args=(),
    kwargs={}, *, daemon=None)'''
    
    t1=threading. Thread(target=print_thread, args=("Thread1", 1))#args are the arguments that the function takes as input
    t2=threading. Thread(target=print_thread, args=("Thread2", 1))

    t1.start() #starts the thread
    t2.start()

    
    t1.join() #wait till the execution of the thread is completed
    t2.join()
    
    print("Exit threading")

