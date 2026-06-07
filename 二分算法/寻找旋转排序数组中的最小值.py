def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

if __name__ == "__main__":
    nums = list(map(int, input().split()))

    result = findMin(nums)
    print(result)