A = [3, 5, 2, 7, 1, 4, 6, 8]

N = len(A)

size = 1
while size < N:
    size *= 2

seg = [0] * (2 * size)

# 葉にAの値を入れる
for i in range(N):
    seg[size + i] = A[i]

# 下から順番に親を計算
for i in range(size - 1, 0, -1):
    seg[i] = seg[2 * i] + seg[2 * i + 1]
    print(seg)
print(size)
print(seg)