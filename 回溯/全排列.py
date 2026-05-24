def backtracking(nums, used, path, result):
    if len(path) == len(nums):
        result.append(path[:])
        return result
    for i in range(len(nums)): 
        if used[i] == False:
            used[i] = True
            path.append(nums[i])
            backtracking(nums, used, path, result)
            used[i] = False
            path.pop()
        else:
            continue

def permute(nums):
    path = []
    result = []
    used = [False] * len(nums)
    backtracking(nums, used, path, result)
    return result
        
if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    result = permute(nums)
    print(result)