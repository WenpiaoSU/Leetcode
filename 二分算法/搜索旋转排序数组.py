# 从任意位置将数组一分为二，其中一半必定是有序的，另一半则是部分有序（包含旋转断点）
def findTarget(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # 左半边[left, mid]有序
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # 右半边[mid, right]有序
        else:
            if nums[mid] < target <= nums[right]:
                left  = mid + 1
            else:
                right = mid - 1
    return -1

