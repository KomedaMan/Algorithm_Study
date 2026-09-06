A, B, M = map(int, input().split())
def test(A, B, M):
    ans = 1
    while B > 0:
        if B & 1 == 1:
            ans = (ans * A) % M
        A = (A * A) % M
        B = B >> 1
    return ans
a = test(A, B, M)
print(a)