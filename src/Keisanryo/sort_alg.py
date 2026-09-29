# ソートの基本
A = [5, 2, 4, 1, 3]
A.sort()
"""
昇順にしている
降順にしたい場合
.sort(reverse=True)
key引数に各要素に適用する関数を指定できる
key=len, str.lower（大文字小文字区別しない場合）, abs（絶対値でソート）
文字列は文字コード順になる？
"""
print(A)
# 最小の差を求める
ans = min(A[i+1] - A[i] for i in range(len(A)-1))
print(ans)


"""
二次元リストにおいて先頭以外の要素でソートしようと思うとこのようになる。

n = int(input())  # nは入力回数
str_list = [list(input().split()) for _ in range(n)]
print(sorted(str_list,key=lambda x:x[1]))  # 2番目の要素でソート

[入力]
3
az aj
ab aa
bc ad

[参照]
https://qiita.com/ell/items/ea904c898e0e00ff2e24
"""