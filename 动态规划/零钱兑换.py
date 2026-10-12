# 和完全平方数思路相同
# amount相当于n
# coins相当于完全平方数
# dp[i] = 凑成金额i所需最少硬币个数
# 没有硬币能组成amount：dp[amount] = inf

def coinChange(coins, amount):
    dp = [inf] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)
    if dp[amount] < inf:
        return dp[amount]
    else:
        return -1