# 回溯+剪枝
# 不能同行，不能同列，不能同对角线
# 记录已经使用过的列cols
# 已经用过的对角线diag1：row - col相同
# 已经用过的对角线diag2：row + col相同
# 遍历每一行开始放皇后

# 输入n
# 输出[['.Q..', '...Q', 'Q...', '..Q.'], ...]

def main(n):
    result = []
    # 记录列、主对角线、副对角线
    cols = set()
    diag1 = set()
    diag2 = set()
    # 初始化棋盘
    board = [["." for _ in range(n)] for _ in range(n)]
    def dfs(row):
        if row == n:   # 已经遍历到最后一行
            temp = [''.join(board[i]) for i in range(n)]
            print(temp)  # temp代表一种解决方案 ['.Q..', '...Q', 'Q...', '..Q.']
            result.append(temp)
            return
        # 枚举列
        for col in range(n):
            # 剪枝
            if col in cols:
                continue
            if (row - col) in diag1:
                continue
            if (row + col) in diag2:
                continue
            # 放置皇后
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # 继续下一行
            dfs(row+1)
            # 回溯
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    dfs(0)
    return result
if __name__ == "__main__":
    n = int(input().strip())
    result = main(n)
    for solution in result:
        for row in solution:
            print(row)
        print()