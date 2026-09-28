A = [1,3,5,7,9]

def binary_search(x):
    l, r = 0, len(A)
    while l < r:
        mid = (l + r) // 2
        if A[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

print(binary_search(6))  # 挿入位置