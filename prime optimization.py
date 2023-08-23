import math
import time
def isPrimeOptimal(n):
    sa = int(math.sqrt(n))
    count = 0
    for i in range(2, sa+1):
        if n % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False
    
def isPrimeJoke(n):
    
    count = 0
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False
    
num = int(input("enter a num: "))
def timeElapsed(func, *args):
    st = time.time()
    
    a = func(*args)
    et = time.time()
    return a, et - st
print(timeElapsed(isPrimeJoke,num))
# print(timeElapsed(isPrimeOptimal,num))


        
    