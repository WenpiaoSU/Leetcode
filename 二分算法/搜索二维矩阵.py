# 把矩阵每一行拼在一起，可以得到一个递增数组
# left从 0 开始，right从 m*n-1 开始
# 如何还原回矩阵的位置？
# 行 mid // n；列 mid % n

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // n][mid % n]
        if mid_val > target:
            right = mid - 1
        elif mid_val < target:
            left = mid + 1
        else:
            return True
    return False

if __name__ == "__main__":
    # 输入首行：m n
    # 然后输入多行是矩阵的每行内容
    m, n = map(int, input().split())   # 行列
    target = int(input())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    
    print(matrix)

    print("True" if searchMatrix(matrix, target) else "False")
    