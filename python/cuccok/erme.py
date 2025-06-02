import random as rd
import collections as cls
import time as t

def coin(n: int, k: int):
    """simulates flipping a coin"""

    lst = []
    t0 = t.time()
    print('started')
    while len(lst) < k:
        b = 0
        for _ in range(n): b += rd.randint(0, 1)
        lst.append(b)
    def count(lst): return cls.Counter(lst)
    counter = count(lst); x = (counter.most_common(1))
    print(f"A leggyakoribb fejszám: {x[0][0]}, és ez {x[0][1]} esetben fordult elő.")
    print(f"{t.time()-t0} s")

if __name__ == "__main__":
    #n  = int(input("Kérek egy egész számot légyszi. ")); k  = int(input("Mégegyet légyszi. "))
    n = 10000; k =100
    coin(n, k)

