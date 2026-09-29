# 合計が K=7 以下になる連続部分配列が何個あるか
A = [1, 2, 3, 4, 5]
K = 7       #合計の上限

l = 0       # 左端
total = 0   #l～r の範囲の合計
ans = 0     #条件を満たす連続区間の個数

for r in range(len(A)):     # r:右端
    total += A[r]

    while total > K:
        total -= A[l]
        l += 1

    ans += (r - l + 1)

print(ans)