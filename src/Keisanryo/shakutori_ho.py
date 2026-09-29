A = [1, 2, 3, 4, 5]
K = 7

l = 0
total = 0
ans = 0

for r in range(len(A)):
    total += A[r]

    while total > K:
        total -= A[l]
        l += 1

    ans += (r - l + 1)

print(ans)