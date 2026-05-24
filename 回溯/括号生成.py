# n:生成括号的对数，例如((()))
# 返回所有可能的括号组合

# 解法：决策树，每一步选择( or )
# 左括号的总数不能超过n
# 当前的右括号数量不能超过当前的左括号数量
# 递归终止：当前字符串长度=2n，放入结果集

def backtracking(s, left, right, n, res):
    if len(s) == 2 * n:
        res.append(s)
        return
    if left < n:
        s += '('
        backtracking(s, left+1, right, n, res)
        s = s[:-1]
    if right < left:
        s += ')'
        backtracking(s, left, right+1, n, res)
        s = s[:-1]
def generateParenthesis(n):
    res = []
    s = ""
    left = 0  # 当前左括号的数量
    right = 0  # 当前右括号的数量
    backtracking(s, left, right, n, res)
    return res

if __name__ == '__main__':
    n = int(input())
    result = generateParenthesis(n)
    print(result)
