# 统计每个元素出现频率{元素：频率}
# 按照频率构建小顶堆heap
# 和第K个最大元素的解法一样，当heap长度大于K时，弹出
# 记录小顶堆中剩下的元素
from collections import defaultdict
import heapq

def topKFrequent(nums, k):
    cnt = defaultdict(int)
    # {元素：出现频率}
    for x in nums:
        cnt[x] += 1
    heap = []  # 小顶堆
    for key, value in cnt.items():
        # 按照（频率，元素）入堆
        heapq.heappush(heap, (value, key))
    while len(heap) > k:
        heapq.heappop(heap)
    ans = [0] * k
    for i in range(k):
        ans[i] = heap[i][1]
    return ans