# 所有可达路径
def dfs(graph, x, n, path, result):
    if x == n:    # 当前节点已到达目标节点n
        result.append(path[:])
        return
    for i in range(1, n + 1):    # x是当前节点，i是x可能指向的节点
        if graph[x][i] == 1:   # 从节点x到i是否有路径
            path.append(i)
            dfs(graph, i, n, path, result)  # 递归进入下一个节点
            path.pop()
def main():
    n, m = map(int, input().split())   # n是节点数，m是边数
    graph = [[0] * (n+1) for _ in range(n+1)]
    # 构建邻接矩阵
    for _ in range(m):
        s, t = map(int, input().split())   # 读入每一行的两个节点
        graph[s][t] = 1

    result = []
    dfs(graph, 1, n, [1], result)

    # 打印结果
    if not result:
        print(-1)
    else:
        for path in result:
            print(' '.join(map(str, path)))

if __name__ == '__main__':
    main()