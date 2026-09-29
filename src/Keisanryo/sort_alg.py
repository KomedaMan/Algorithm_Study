# ソートの基本
A = [5, 2, 4, 1, 3]
A.sort()
print(A)
# 最小の差を求める
ans = min(A[i+1] - A[i] for i in range(len(A)-1))
print(ans)