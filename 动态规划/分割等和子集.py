# 找到 nums 里哪个子集总和为 sum/2
# dp[j]：是否可以从nums中选出子集，使其和为j

def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        # 内层循环必须从后往前遍历，防止一个数字被使用多次 (0-1背包的特性)
        # 只需要遍历到 num 即可，因为 i < num 时，连这个数字本身都放不下
        for i in range(target, num-1, -1):
            dp[i] = dp[i] or dp[i-num]
        # 提前优化：如果此时 dp[target] 已经为 True，说明已经找到了解，可以直接返回
        if dp[target]:
            return True
    return dp[target]