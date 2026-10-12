# dp[i] 和为 i 的完全平方数的最少数量。
# dp[i] = dp[i - (j**2)] + 1
# j**2是指一个完全平方数，+1是把这个数量加上
# 尝试所有可能的j(j**2从 1 到 n)，取数量最小值dp[i] = min(dp[i], dp[i-j*j] + 1)

def numSquares(n):
    dp = [inf] * (n+1)
    # dp下标从 0 到 n
    dp[0] = 0
    for i in range(1, n+1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[n]
    

