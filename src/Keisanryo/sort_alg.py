# ソートの基本
A = [5, 2, 4, 1, 3]
A.sort()
"""
昇順にしている
降順にしたい場合
.sort(reverse=True)
key引数に各要素に適用する関数を指定できる
key=len, str.lower（大文字小文字区別しない場合）
"""
print(A)
# 最小の差を求める
ans = min(A[i+1] - A[i] for i in range(len(A)-1))
print(ans)