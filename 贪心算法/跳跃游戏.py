def canJump(nums):
    cur_max = 0
    for i in range(len(nums)):
        if i > cur_max:  # 当前索引超出了能到达的最大位置
            return False
        # 更新能到达的最远距离
        if i + nums[i] > cur_max:
            cur_max = i + nums[i]
        # 能到达最后一个下标
        if cur_max >= len(nums) - 1:
                return True
    return False
