from collections import Counter, defaultdict

def findAnagrams(s: str, p: str):
    if len(s) < len(p):
        return []
    cnt_p = Counter(p)
    cnt_s = defaultdict(int)  # 统计s中长为p的子串的每种字母出现次数
    ans = []
    n = len(p)
    for right, c in enumerate(s):
        cnt_s[c] += 1  # 右端点进入
        left = right - n + 1
        if left < 0:  # 窗口长度不足n
            continue
        if cnt_s == cnt_p:  # 子串中和p中的字母出现次数都相同
            ans.append(left)  # 将子串左端点下标加入
        out = s[left]
        cnt_s[out] -= 1  # 左端点出
        if cnt_s[out] == 0:
            del cnt_s[out]
    return ans

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    result = findAnagrams(s, p)
    print(result)