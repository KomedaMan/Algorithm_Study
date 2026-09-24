import math

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
B = int(math.sqrt(N))   # 平方根をとる
# print(N, B)
# N:10, B:3

# ブロックデータを作成
block_sum = [0] * ((N+B-1)//B)
# block_sum:[0, 0, 0, 0]

# 前処理
for i in range(N):
    block_sum[i//B] += A[i]
# print(block_sum)
# [6, 15, 24, 10]

# 区間和
def query(l, r):    # 区間の左側の要素番号:l、右側の要素番号:r
    res = 0
    # 0-indexのため計算が行われる終値はr-1となる。そのため条件はl<r
    while l < r:
        # ブロック毎に計算する場合（lとブロックの要素数を足してもrに届かない場合）
        if l % B == 0 and l + B <= r:
            res += block_sum[l//B]
            l += B
        # lがブロックの先頭に行くまでとlとrの間がブロックの要素数に満たない場合
        else:
            res += A[l]
            l += 1
    return res

print(query(2, 8))
# 33

# 個の場合の指定される要素は3,4,5,6,7,8
print(3+4+5+6+7+8)
# 33