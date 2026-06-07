def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid + 1
    # 此时left指向第一个位置
    return left
def searchRange(nums, target):
    start = lower_bound(nums, target)
    if start == len(nums) or nums[start] != target:
        return [-1, -1]
    end = lower_bound(nums, target+1) - 1
    return [start, end]

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    # 控制台输入
    # nums = list(map(int, input().split()))
    # target = int(input())
    result = searchRange(nums, target)
    print(result)