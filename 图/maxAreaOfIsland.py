# 最大岛屿面积
def dfs(grid, i, j):
    if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1)


def main():
    m, n = map(int, input().split())  # 矩阵行列数
    grid = []
    for i in range(m):
        grid.append(list(map(int,input().strip())))  # 读入一行，并转换为整数列表

    maxArea = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count = dfs(grid, i, j)
                maxArea = max(maxArea, count)
    print(maxArea)

if __name__ == "__main__":
    main()