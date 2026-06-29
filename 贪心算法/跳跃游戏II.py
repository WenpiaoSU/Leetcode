def jump(nums):
    step = 0
    cur_max = 0  # 当前能跳到的最远位置
    max_len = 0  # 在当前能跳到的这些位置里，往后跳能跳到的最远距离
    for i in range(len(nums)-1):
        max_len = max(max_len, i + nums[i])
        if i == cur_max:  # 到达了当前步的边界
            step += 1
            cur_max = max_len   # 更新边界为刚才找到的最远距离
    return step
        
        