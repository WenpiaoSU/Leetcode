# 动态规划 0--i 的乘积最大子数组
# 若当前遍历的数是正数，则取max(nums[i], i-1的乘积最大子数组)
# 若当前遍历的数是负数，则取max(nums[i], i-1的乘积最小子数组)
# 负数只有乘较小的数，才能保持大
# 因此，在遍历时维护两个变量，最大乘积fmax[i], 最小乘积fmin[i]
# fmax[i] = max(nums[i], fmax[i-1] * nums[i], fmin[i-1] * nums[i])
# fmin[i] = min(nums[i], fmax[i-1] * nums[i], fmin[i-1] * nums[i])
# 这样，若i前面的乘积是0或负数，则在i时可以重新算

from math import inf

def maxProduct(nums):
    if not nums:
        return 0
    res = fmax = fmin = nums[0]
    for i in range(1, len(nums)):
        temp_fmax = fmax
        fmax = max(nums[i], fmax * nums[i], fmin * nums[i])
        fmin = min(nums[i], temp_fmax * nums[i], fmin * nums[i])
        res = max(res, fmax)
    return res
