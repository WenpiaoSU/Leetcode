# 数组长度奇数：中位数是中间的数；偶数：中位数是中间两个的平均值
# 建立一个小顶堆A和大顶堆B，各保存列表的一半元素
# A保存大的一半，堆顶可能就是中间值
# B保存小的一半，堆顶可能就是中间值
# 假设共有N = m + n个元素
# A是m个元素 ，B是n个元素，保证m = n + 1 or = n
# 中位数是A的堆顶或者是（A堆顶+B堆顶）/ 2

import heapq


class MedianFinder:
    def __init__(self):
        self.A = []  # 小顶堆，存大的一半
        self.B = []  # 大顶堆，存小的一半（注：大顶堆是小顶堆取负数）
    
    def addNum(self, num):
        if len(self.A) != len(self.B):
            # 将新元素 num 插入至 A ，再将 A 堆顶元素插入至 B
            heapq.heappush(self.A, num)
            heapq.heappush(self.B, -heapq.heappop(self.A))
        else:
            # 将新元素 num 插入至B，再将B堆顶元素插入A
            heapq.heappush(self.B, -num)
            heapq.heappush(self.A, -heapq.heappop(self.B))
    
    def findMedian(self):
        if len(self.A) == len(self.B):
            return (self.A[0] - self.B[0]) / 2.0
        else:
            return self.A[0]
        
    