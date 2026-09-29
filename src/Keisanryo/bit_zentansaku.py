# bit全探索
N = 3
A = [1,2,3]

for bit in range(1 << N):
    subset = []
    for i in range(N):
        if bit & (1 << i):
            subset.append(A[i])
    print(subset)
print(1 << N)
"""
<< は左シフトの演算子
>> は右シフトの演算子
元　<< シフト回数？
"""