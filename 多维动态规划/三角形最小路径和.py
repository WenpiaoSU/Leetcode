import sys

def minimumTotal(triangle):
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
    for i in range(2, len(triangle)):
        for j in range(1, len(triangle[i])-1):
            dp[i][j] = min(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
    return min(dp[-1])

if __name__ == '__main__':
    # 输入第一行是三角形的行数，后面是每一行的内容
    # 输入完之后按ctrl+z再按enter输出
    input = sys.stdin.read().strip().split()
    print(f"input:{input}")   # ['4', '2', '3', '4', '6', '5', '7', '4', '1', '8']
    n = int(input[0])
    nums = list(map(int, input[1:]))   # [2, 3, 4, 6, 5, 7, 4, 1, 8]
    print(f"nums:{nums}")
    triangle = []
    idx = 0
    for i in range(n):
        row = nums[idx : idx + i + 1]
        triangle.append(row)
        idx += i + 1
    print(f"triangle:{triangle}")   # [[2], [3, 4], [6, 5, 7], [4, 1, 8]]
    print(minimumTotal(triangle))
        
