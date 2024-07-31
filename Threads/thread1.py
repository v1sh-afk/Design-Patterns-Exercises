import _thread
import time

def print_thread(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "---------", time.time())
    print("Exit")

#_thread.start_new_thread ( function, args[, kwargs] )
    
_thread.start_new_thread(print_thread,("thread 1", 1))
_thread.start_new_thread(print_thread,("thread 2", 3))










'''try:

    _thread.start_new_thread(print_thread, ("thread 1", 2))
    _thread.start_new_thread(print_thread, ("thread 2", 4))
except:
    print("this is an error")

while 1:
    pass'''
