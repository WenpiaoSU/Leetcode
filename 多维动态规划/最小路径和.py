import sys

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
    return dp[m-1][n-1]

if __name__ == "__main__":
    input = sys.stdin.read().strip().split()
    print(f"输入：{input}")
    # 输入：['3', '3', '1', '3', '1', '1', '5', '1', '4', '2', '1']
    m = int(input[0])  # 行数
    n = int(input[1])  # 列数
    nums = list(map(int, input[2:]))
    grid = []
    idx = 0
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(nums[idx])
            idx += 1
        grid.append(row)
    print(f"grid:{grid}")
    # grid:[[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = minPathSum(grid)
    print(f"最终结果：{result}")
    # 最终结果：7