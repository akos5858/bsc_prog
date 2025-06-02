def node_weight(edges: list) -> dict:
    """node weights from edge weights"""
    d = {}
    for a, b, w in edges:
        d[a] = w + d.get(a, 0)
        if not a == b:
            d[b] = w + d.get(b, 0)
    return d


def test_node_weight():
    edges_t1 = []
    edges_t2 = [(1, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 1, 1)]
    edges_t3 = [(1, 2, 1), (1, 3, 1), (2, 3, 1), (2, 4, 1), (3, 4, 1)]
    edges_t4 = [(1, 2, 1), (1, 3,-4), (2, 3, 1), (2, 4,-4), (3, 4, 1)]
    edges_t5 = [(1, 2, 1), (1, 3, 1), (1, 3,-1), (2, 3, 1), (2, 3,-1)]

    assert node_weight(edges_t1) == {}
    assert node_weight(edges_t2) == {1: 3, 2: 2, 3: 2, 4: 2}
    assert node_weight(edges_t3) == {1: 2, 2: 3, 3: 3, 4: 2}
    assert node_weight(edges_t4) == {1:-3, 2:-2, 3:-2, 4:-3}
    assert node_weight(edges_t5) == { 1 : 1, 2 : 1, 3 : 0  }


if __name__ == "__main__":
    
    try: test_node_weight()
    except AssertionError: print('test failed')
    else: print('tests succeded')

    edges =  [(100, 200, 1), (100, 200, 2), (100, 1, -1), (1, 1, 5)]
    #print(node_weight(edges))
 