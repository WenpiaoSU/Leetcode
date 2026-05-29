# s = "aab"
# output = [["a", "a", "b"], ["aa", "b"]]
# 先按照所有可能的方式进行分割
# 判断分割出的子串是否是回文串
# 解法：回溯枚举切割位置
# 假设当前处理位置start，枚举结束位置end，判断 s[start:end+1] 是否是回文串
    # 如果是，则加入当前路径，递归处理后面的位置
# start == len(s)，说明整个字符串已经被切割完成，把当前方案加入最终结果
# 回文判断：sub == sub[::-1]

def backtracking(s, start, path, result):
    if start == len(s):
        result.append(path[:])
        return
    for end in range(start, len(s)):
        if s[start: end + 1] == s[start: end + 1][::-1]:   # 该子串是回文串
            path.append(s[start: end+1])
            backtracking(s, end+1, path, result)
            path.pop()

if __name__ == "__main__":
    s = input().strip()
    result = []
    backtracking(s, 0, [], result)
    for item in result:
        print(' '.join(item))
