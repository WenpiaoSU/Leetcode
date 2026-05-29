# 找到目标值 → 返回下标
# 找不到目标值 → 返回插入位置
# 要求时间复杂度：O(log n)

def findTarget(nums, target):
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return left        

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    
    result = findTarget(nums, target)
    print(result)