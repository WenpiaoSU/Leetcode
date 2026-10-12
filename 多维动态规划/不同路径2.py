import sys

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    # 1:障碍物   0:可走的位置
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    # 第一列初始化
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    # 第一行初始化
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
    
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
    return dp[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read().strip().split()
    input = list(map(int, input))
    m = input[0]
    n = input[1]
    nums = input[2:]
    idx = 0
    obstacleGrid = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(nums[idx])
            idx += 1
        obstacleGrid.append(row)
    print(f"obstacleGrid:{obstacleGrid}")
    print(uniquePathsWithObstacles(obstacleGrid))