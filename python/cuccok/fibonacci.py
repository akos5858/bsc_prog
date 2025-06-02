from time import time

def fibonacci(n: int) -> int:
    """computes the n-th fibonacci number"""
    if n >= 0: 
        a = b = 1
        for _ in range(1, n): a, b = b, a+b
        return b


if __name__ == "__main__":

    t = time()
    print('started')
    f = (fibonacci(350000))  
    print(f)
    print(f'ended in {time()-t} s') 

    """
    t = time()
    a = (fibonacci(10**3))  
    print(f'ended in {time()-t} s') 

    t = time()
    a = (fibonacci(10**4)) 
    print(f'ended in {time()-t} s') 

    t = time()
    a = (fibonacci(10**5))  
    print(f'ended in {time()-t} s') 

    t = time()
    a = (fibonacci(10**6))  
    print(f'ended in {time()-t} s') 

    #t = time()
    #a = (fibonacci(10**7))  
    print(f'ended in {time()-t} s') 

    """
