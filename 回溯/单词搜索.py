# board 二维字符网格
# word 字符串单词
# 判断word是否存在board中（有连续的路径组成word）
# 解法：先遍历每一个格子，找可能的起点；然后尝试匹配word的第k个字符
# 终止：如果k=word长度，说明全部匹配成功，true
def backtracking(r, c, k, word, board):
    if k == len(word):
        return True
    # 不满足条件：越界 or 当前位置不等于word对应位置
    if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[k]:
        return False   # 此路不通
    temp = board[r][c]
    board[r][c] = '#'   # 标记为特殊字符，代表这里遍历过了
    # 继续朝四个方向深度遍历，有一个方向为true就可以
    res = backtracking(r+1, c, k+1, word, board) or backtracking(r-1, c, k+1, word, board) or backtracking(r, c+1, k+1, word, board) or backtracking(r, c-1, k+1, word, board)
    # 回溯
    board[r][c] = temp
    return res

def exist(board, word):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if backtracking(r, c, 0, word, board):
                return True
    return False

if __name__ == "__main__":
    word = 'ABCCED'
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    res = exist(board, word)
    print(res)