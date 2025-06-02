def gcd(a: int, b: int) -> int:
    """computes the greatest common divisor"""
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

if __name__ == "__main__":
    a = 12
    b = -3

    print(gcd(a, b))
    print(lcm(a, b))

