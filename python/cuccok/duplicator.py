def duplicator(l):
    """duplicates each element of a list"""
    l[:0] = l[::2] = l[1::2] = l[:]
    return l

l = [0, 1, 1, (0, 1),'a', True, None, {}, set()]
if __name__ == "__main__":
    print(duplicator(l))
