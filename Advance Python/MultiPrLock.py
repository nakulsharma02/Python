# MultiProcessing Lock
'''The multiprocessing.Lock in Python is a synchronization primitive used to manage access to shared resources among multiple processes. It ensures that only one process can access a critical section of code or a shared resource at any given time, preventing race conditions and maintaining data integrity.'''

# Without lock showing Inconsistent Behaviour means give different Output on The same Input While Running Multiple Times But the Correct Output is One
'''import time 
import multiprocessing
def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1
def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1 
if __name__=="__main__":
    balance = multiprocessing.Value('i',200)
    d = multiprocessing.Process(target=deposit,args=(balance,))
    w = multiprocessing.Process(target=withdraw,args=(balance,))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
'''

# Use of MultiProcessing Lock
import time
import multiprocessing
def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value= balance.value + 1
        lock.release()
def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target = deposit,args=(balance,lock))
    w = multiprocessing.Process(target=withdraw,args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
''' It always give O/P 200 when Executing'''