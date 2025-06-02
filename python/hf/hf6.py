#import pytest as pt

def cycle(lst: list) -> tuple:
    final = []

    def ciklus(lst):
        b = lst[i]
        new = [i]
        while b != i:
            new.append(b)
            b = lst[b]
        return new

    for i in range(len(lst)):
        if min((ciklus(lst))) == ciklus(lst)[0] and len(ciklus(lst)) != 1:
            final.append(ciklus(lst))

    return [tuple(x) for x in final]

class Permutation:

    def __init__(self, lst: list):
        self.seq = lst
        if set(range(len(self.seq))) != set(self.seq):
            raise ValueError('nem Permutáció')
        else: 
            self.cycles = sorted(cycle(lst))

    def __repr__(self):
        return f"{type(self).__name__}({list(self.seq)})"

    def __str__(self):
        return f"cycles : {self.cycles}"


if __name__ == "__main__":
    pi0 = Permutation([1, 2, 3, 0])
    print(repr(pi0))
    print(pi0)

    pi1 = Permutation([1, 0, 3, 2])
    print(repr(pi1))
    print(pi1)


"""
def test_cycles():

    with pt.raises(ValueError):
        Permutation([1, 2, 3, 4])
        Permutation([1, 1, 0, 2])

    pi0 = Permutation([1, 2, 3, 0])
    assert print(repr(pi0)) == 'Permutation([1, 2, 3, 0])'
    assert print(pi0)       == 'cycles : [(0, 1, 2, 3)]'

    pi1 = Permutation([1, 0, 3, 2])
    assert print(repr(pi1)) == 'Permutation((1, 0, 3, 2))'
    assert print(pi1)       == 'cycles : [(0, 1), (2, 3)]'
    
try: test_cycles()
except AssertionError: print('test failed')
else: print('tests succeded')
"""


