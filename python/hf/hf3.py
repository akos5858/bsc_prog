def max_prod(lst : list, k : int) -> float:
    "megkeresi egy lista azt a k hosszú részsorozatát, mely elemeinek szorzata maximális"
    prods = 1
    max_prod_yet = 1
    if max(lst) == 0 and min(lst) >= 0:
        max_prod_yet = 0
        return max_prod_yet
    else:   
        for i in range(0, len(lst)-k+1):
            for x in lst[i: k+i]:
                prods *= x
            if prods > max_prod_yet:
                max_prod_yet = prods
            prods = 1
    return max_prod_yet

def test_max_prod():
    try:
        assert max_prod([0, 0, 0, 0], 2)      == 0
        assert max_prod([1,-2, 1, 5, -10], 3) == 1
        assert max_prod([0, -1, -2], 2)       == 2
    except AssertionError as exception:
        print("test failed")
        raise exception
    else:
        print("test succeded")

if __name__ == "__main__":
    print(max_prod([1.1, 2, 2**1, 2.99, 3**0.5, 3], 1))
    test_max_prod()