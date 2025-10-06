# MultiProcessing Pool
'''The multiprocessing.Pool class in Python's multiprocessing module provides a convenient way to manage a pool of worker processes. This pool can be used to parallelize the execution of a function across multiple input values, effectively leveraging multiple CPU cores and bypassing Python's Global Interpreter Lock (GIL) for CPU-bound tasks. And also uilizing Processing power of your Computer'''
# **core = "Processing Units In the CPU"
# First Example shows how it can be executed
'''from multiprocessing import Pool
def f(n):
    return n*n
if __name__ == "__main__":
    array = [1,2,3,4,5]
    p = Pool()
    result = p.map(f,array)
    print(result)
'''
'''O/P = [1,4,9,16,25]'''

# Another Example
'''from multiprocessing import Pool
import time
def f(n):
    sum = 0
    for x in range(1000):
        sum+=x*x 
    return sum
if __name__=="__main__":
    t1=time.time()
    p=Pool()
    result = p.map(f,range(10000))
    p.close()
    p.join()
    print("Pool took :",time.time()-t1)
    t2 = time.time()
    result=[]
    for x in range(10000):
        result.append(f(x))
    print("Serial Processing took:",time.time()-t2)
'''
'''Pool take less time as compare to serial Processing'''

# Pool Arguments
from multiprocessing import Pool
def f(n):
    return n*n
if __name__=="__main__":
    p=Pool(processes=3)
    result=p.map(f,[1,2,3,4,5])
    for n in result:
        print(n)
'''O/P = 
1
4
9
16
25
'''