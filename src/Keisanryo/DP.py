# DP 動的計画法
N = 10
dp = [0]*(N+1)

dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])