# Executing Multiple SubProcessess At time of execution of the program
'''For a Given List of Numbers print Square and cube of every numbers'''
import time 
import threading
def calc_square(numbers):
    print("Calculate Square of Numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f"Square of {n} is {n*n}")
def calc_cube(numbers):
    print("Calculate Cube of Numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f"Cube of {n} is {n*n*n}")
arr = [2,3,4,5]
t = time.time()
t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(end-t)
'''def calc_square(numbers):
    print("Calculate Square of Numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f'Square of {n} is {n*n}')
def calc_cube(numbers):
    print("Calculate Cube of Numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f'Cube of {n} is {n*n*n}')
arr=[2,3,4,5]
start = time.time()
calc_square(arr)
calc_cube(arr)
end = time.time()
print("Time:", end - start)'''