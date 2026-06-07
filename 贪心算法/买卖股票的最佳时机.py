# 枚举右，维护左：低价买入，高价卖出。
# 在0到i-1间求最小值，用min_price维护
# 每次枚举i，最大利润 = prices[i] - min_price

def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    for p in prices:
        max_profit = max(max_profit, p - min_price)
        min_price = min(min_price, p)
    return max_profit

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    print(maxProfit(prices))