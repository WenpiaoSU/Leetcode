# 判断图是否联通（从节点1出发）
def dfs(graph, key, visited):
    # key 是节点，visited是访问状态
    for i in graph[key]:
        if not visited[i]:  # 如果没访问过该节点
            visited[i] = True  # 记为访问过
            dfs(graph, i, visited)


def main():
    m, n = map(int, input().split())
    # 建立邻接表
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, t = map(int, input().split())
        graph[s].append(t)

    visited = [False] * (n + 1)
    visited[1] = True

    dfs(graph, 1, visited)

    # 检查是否所有节点都被访问
    for i in range(1, n + 1):
        if not visited[i]:
            print(-1)
            return
    print(1)


if __name__ == "__main__":
    main()