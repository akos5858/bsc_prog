import random as rd
from itertools import islice
import pytest as pt


class RandomNames:
    
    def __init__(self, names):
        self.names = names 

    def __repr__(self):
        print(self._names)

    def __iter__(self):
        self._names_copy = self._names.copy()
        while True:
            rd.shuffle(self._names_copy)
            yield from self._names_copy
                
    def __call__(self):
        return rd.choice(self._names)

    @property
    def names(self):
        return self._names
   
    @names.setter
    def names(self, new_value):
        if isinstance(new_value, str):
                raise ValueError
        for new_name in new_value:
            if not isinstance(new_name, str):
                raise ValueError
        cache = []
        for name in new_value:
            cache.append(name.lower().capitalize())
        self._names = cache


def test_random_names():
    rn = RandomNames(['anDoR'])
    assert rn.names == ['Andor']
    rn.names = ['ALADÁR', 'elemér']
    assert rn.names == ['Aladár', 'Elemér']
    rn.names = ['ALADÁR', 'elemér', 'Béla', 'Cecil', 'Dezső', 'Ferenc', 'GÉZA', 'Huba', 'imre', 'Jenő', 'Kálmán', 'LAci', 'Miklós', 'NándoR', 'OTTÓ', 'Pista', 'ReZSő', 'Sándor', 'Teréz', 'ubul', 'VILMos', 'Zoltán']
    assert rn() != rn()
    assert set(islice(rn, len(rn.names))) == set(rn.names)
    assert tuple(islice(rn, len(rn.names))) != tuple(rn.names)
    rn.names = ['ALADÁR', 'elemér']
    assert rn.names == ['Aladár', 'Elemér']
    with pt.raises(ValueError):
        rn = RandomNames("Péter")
        rn.names = [0]

if __name__ == "__main__": 
    try: test_random_names()
    except AssertionError: print('test failed')
    else: print('tests succeded')

