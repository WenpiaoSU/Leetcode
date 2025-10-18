# 岛屿数量
import sys
sys.setrecursionlimit(100000)  # 避免DFS递归深度问题

def dfs(grid, i, j):
    if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
        return
    grid[i][j] = '0'  # 置为零，防止重复遍历
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)


def main():
    # 从控制台读取输入
    n, m = map(int, input().split())  # 矩阵行列数
    grid = []
    for i in range(n):
        grid.append(list(input().strip()))

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    print(count)


if __name__ == "__main__":
    main()