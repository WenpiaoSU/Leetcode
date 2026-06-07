# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
import heapq


def findKthLargest(k, nums):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]

if __name__ == "__main__":
    input = list(map(int, input().split()))
    k = 2
    print(input)
    output = findKthLargest(k, input)
    print(output)