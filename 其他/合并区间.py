
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    return result

if __name__ == "__main__":
    n = int(input())   # 输入区间数量
    intervals = []
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append([start, end])
    result = merge(intervals)
    print(result)