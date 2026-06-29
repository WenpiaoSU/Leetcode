def rob(nums):
    if len(nums) == 0:  # 如果没有房屋，返回0
        return 0
    if len(nums) == 1:  # 只有一个房屋，就偷他自己！
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[len(nums)-1]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(rob(nums))

