def generate(numRows):
    c = [[1] * (i+1) for i in range(numRows)]  # 全1填充
    for i in range(2, numRows):  # 从第2行开始
        for j in range(1, i):  # 中间需要计算的部分
            # 左上方的数+正上方的数
            c[i][j] = c[i-1][j-1] + c[i-1][j]
    return c
    