# 比较 nums[mid] 和 nums[mid + 1]
# nums[mid] < nums[mid + 1]：当前处于上坡，峰值一定在mid右侧，left = mid + 1
# nums[mid] > nums[mid + 1]：当前处于下坡，mid可能是峰值，也可能是峰值的右侧，right = mid
# left == right时就找到了一个峰值

def findPeak(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= nums[mid + 1]:
            left = mid + 1
        elif nums[mid] > nums[mid + 1]:
            right = mid
    return left

if __name__ == "__main__":
    nums = [1, 3, 5, 4, 2]
    result = findPeak(nums)
    print(result)