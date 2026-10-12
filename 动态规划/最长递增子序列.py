# dp[i] 到当前位置i，最长严格递增子序列的长度
# dp[i]等于他之前的最长严格递增子序列的长度 + 1（他自己）
# 之前的用dp[j], 0 <= j < i，去遍历
# 并只取nums[i] > nums[j]的 j


def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:   # 必须是递增
                dp[i] = max(dp[i], dp[j] + 1)   # 加的1是指i占一个长度
    return max(dp)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(lengthOfLIS(nums))
