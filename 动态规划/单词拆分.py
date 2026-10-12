# dp[i]：字符串s的前i个字符（下标 0 到 i-1）是否可以被拆分成字典中的单词
# 找到 0 <= j < i，如果dp[j]为真（前j个可以拆分），且s[j:i]在字典中，则dp[i]为真
def wordBreak(s, wordDict):
    word_list = set(wordDict)
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_list:
                dp[i] = True
                break
    return dp[n]