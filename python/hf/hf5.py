from typing import Sequence

def collect_positions(seq: Sequence) -> dict:
    """Returns for each element in seq the list of occurences"""
    d = {}
    for i, c in enumerate(seq):
        if c not in d: d[c] = [i]
        else: d[c].append(i)
    return d

def test_collect_positions():
    s1 = "ababababab"
    s2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    s3 = map(str.upper, s2)
    s4 = ''

    d1 = {"a": [0, 2, 4, 6, 8], "b": [1, 3, 5, 7, 9]}
    d2 = {"a": [0, 2, 4, 6, 8], "b": [1, 3, 5, 7, 9]}
    d3 = {"A": [0, 2, 4, 6, 8], "B": [1, 3, 5, 7, 9]}
    d4 = {}

    try:
        assert collect_positions(s1) == d1
        assert collect_positions(s2) == d2
        assert collect_positions(s3) == d3
        assert collect_positions(s4) == d4
    except AssertionError as exception:
        print("test failed")
        raise exception
    else: print('tests succeeded')


if __name__ == "__main__":
    print(collect_positions("ababcda"))
    test_collect_positions()


