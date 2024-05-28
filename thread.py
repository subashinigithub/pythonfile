
#multi-threading
import threading
import time 
def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)
def print_letters():
    for char in['a','b','c','d','e']:
        print(char)
        time.sleep(1)

thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished")
#thread
import threading
import time 
def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_numbers)
thread2.start()
thread1.start()
thread1.join()
thread2.join()