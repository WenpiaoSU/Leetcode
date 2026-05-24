def backtracking(candidates, target, sum, index, path, result):
    # sum: 当前路径总和
    # 若当前路径总和已经超过target，后面继续相加就更大，不需要继续加了
    if sum > target:
        return
    if sum == target:
        result.append(path[:])
        return
    for i in range(index, len(candidates)):
        sum += candidates[i]
        path.append(candidates[i])
        # 由于题目允许重复选取同一个数字，因此下一次循环从i开始，而不是i+1
        # 限制只能从当前及之后的数字中选，避免[2, 3], [3, 2]这种重复组合
        backtracking(candidates, target, sum, i, path, result)
        sum -= candidates[i]
        path.pop()

def combinationSum(candidates, target):
    sum = 0
    index = 0
    path = []
    result = []
    backtracking(candidates, target, sum, index, path, result)
    return result

if __name__ == "__main__":
    candidates = [7, 2, 6, 3]
    target = 7
    result = combinationSum(candidates, target)
    print(result)