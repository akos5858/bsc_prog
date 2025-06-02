from typing import Sequence

def rle(seq : Sequence) -> list:
    """"running length algorithm"""

    db = 1
    lst = []
    char = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == char:
            db = db + 1
        else:
            lst.append((char, db))
            char = seq[i]
            db = 1
    lst.append((char, db))
    return lst
 

def test_rle():
    assert rle(range(3)) == [(0, 1), (1, 1), (2, 1)]
    assert rle(['aaa', 'a', 'a', 'a', 1, 1, [0]]) == [('aaa', 1), ('a', 3), (1, 2), ([0], 1)]
    assert rle("aaa") == [('a', 3)]


if __name__ == "__main__":
    try: test_rle()
    except AssertionError: print('test failed')
    else: print('tests succeded')
          


