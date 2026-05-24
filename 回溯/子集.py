# 如果把子集问题、组合问题、分割问题都抽象为一棵树的话，
# 那么组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点。

class Solution:
    def subsets(self, nums):
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result
        
    def backtracking(self, nums, startIndex, path, result):
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()