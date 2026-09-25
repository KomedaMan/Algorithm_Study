N = 8
# 木のサイズ
size = 1
while size < N:
    size *=2

seg = [0]*(2*size)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 更新
def update(i, x):
    i += size
    seg[i] = x
    while i > 1:
        i //=2
        seg[i] = seg[2*i] + seg[2*i+1]

# 区間和 [l, r)
def query(l, r):
    l += size
    r += size
    res = 0
    while l < r:
        if l % 2:
            res += seg[l]
            l += 1
        if r % 2:
            r -= 1
            res += seg[r]
        l //= 2
        r //= 2
    return res

A = [3, 5, 2, 7, 1, 4, 6, 8]
for i in range(len(A)):
    update(i, A[i])

print(seg)
print(query(2, 8))
print(2+7+1+4+6+8)