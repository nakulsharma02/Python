import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__+" took "+str((end-start)*1000)+" milliseconds ")
        return result
    return wrapper
@time_it 
def cal_square(numbers):
    result=[]
    for number in range(numbers):
        result.append(number*number)
    return result
squares = cal_square(45)
print(squares)
@time_it 
def cal_cube(numbers):
    result = []
    for number in range(numbers):
        result.append(number*number*number)
    return result
cubes = cal_cube(15)
print(cubes)