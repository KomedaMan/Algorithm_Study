# ax + by = gcd(a, b)となる方程式のx, yを求める

def extend_gcd(a, b):
    if b != 0:
        c, y, x = extend_gcd(b, a % b)
        y -= (a // b) * x
        return c, x, y  # cはgcd(a, b)となる。
    return a, 1, 0

c, x, y = extend_gcd(2944, 3958)
print(x, y)
# ユーグリッドの互除法を逆から行うようにする。
# c, x, y = extend_gcd(b, a%b)はa%bが0になるまでn回繰り返し、c, y, xを
# n-1回目のextend_gcdに返す。cは変化しない。最後に残る余りがcに入るので、
# cはユーグリッドの互除法で求めた最大公約数の値が入る。
# 1つ前のxにyを代入してyにxを代入していくことを繰り返す。
# これの証明は拡張ユーグリッドの互除法を検索すること
# https://tbasic.org/reference/old/ExEuclid.html