# Computer's CPU handles Multiple Processes at the same time this process is called MultiProcessing on exection
'''import time
import multiprocessing
square_result = []
def calc_square(numbers):
    global square_result
    for n in numbers:
        print('Square'+str(n*n))
        square_result.append(n*n)
        time.sleep(5)
    print('within a process:result'+str(square_result))
if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p1.start()
    p1.join()
    print('result'+str(square_result))
'''

# Sharing Data Btw Processes using Array and Value
# with the help of array
'''import multiprocessing
def calc_square(numbers,result):
    for idx,n in enumerate(numbers):
        result[idx]=n*n
if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    p = multiprocessing.Process(target = calc_square,args=(numbers,result))
    p.start()
    p.join()
    print(result[:])
    '''

# with the help of values 
'''import multiprocessing 
def calc_square(numbers):
    numbers.value=5.67
if __name__ =="__main__":
    numbers = multiprocessing.Value('d',0.0)
    p = multiprocessing.Process(target=calc_square,args=(numbers,))
    p.start()
    p.join()
    print(numbers.value)
'''

# with the help of MultiProcessing Queue in Python
import multiprocessing
def calc_square(numbers,q):
    for n in numbers:
        q.put(n*n)
if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square,args=(numbers,q))
    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())