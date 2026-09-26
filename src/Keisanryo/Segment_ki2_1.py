A = [3, 5, 2, 7, 1, 4, 6, 8]

N = len(A)

# セグメント木の大きさ
size = 1
while size < N:
    size *= 2

# セグメント木
seg = [0] * (2 * size)

# --------------------
# 初期構築
# --------------------

# 葉にAを入れる
for i in range(N):
    seg[size + i] = A[i]

# 親を下から計算
for i in range(size - 1, 0, -1):
    seg[i] = seg[2 * i] + seg[2 * i + 1]


# --------------------
# 値を変更
# --------------------

def update(i, x):
    # A[i]をxに変更する
    i += size
    seg[i] = x

    # 親を更新
    while i > 1:
        i //= 2
        seg[i] = seg[2 * i] + seg[2 * i + 1]


# --------------------
# 区間の合計
# [l, r)
# --------------------

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


# --------------------
# 使用例
# --------------------

print(query(2, 6))
# 2 + 7 + 1 + 4 = 14

update(3, 10)
# A[3]を7から10に変更

print(query(2, 6))
# 2 + 10 + 1 + 4 = 17