import collections

def partitionLabels(s):
    last_index = collections.defaultdict(int)
    for i, x in enumerate(s):
        if x in last_index:
            last_index[x] = max(i, last_index[x])
        last_index[x] = i
    result = []
    start = 0  # 当前子串的开始下标
    end = 0   # 当前子串的结束下标
    for i in range(len(s)):
        end = max(end, last_index[s[i]])
        # 如果当前遍历到的位置就是最远边界
        if i == end:
            result.append(end - start + 1)
            start = end + 1
    return result
            