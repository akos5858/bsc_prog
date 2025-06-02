import random as rd
import numpy as np
import matplotlib.pyplot as plt


print('started')

guess = 0

while rd.randint(0, 1_000_000) != 1:
    guess += 1

print('finished')
print(guess)
