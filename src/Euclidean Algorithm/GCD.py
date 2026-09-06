def gcd(a, b):
    """
    a, bの最大公約数を求める。
    a: int
    b: int
    """
    if b != 0:
        return gcd(b, a % b)
    else:
        return a

# ユーグリッドの互除法によって最大公約数を求められる。
print(gcd(144, 12))