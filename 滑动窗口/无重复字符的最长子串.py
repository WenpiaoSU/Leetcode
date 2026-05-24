class Solution:
    def lengthOfLongestSubstring(self, s: str):
        cnt = set()
        left = 0
        ans = 0
        for right, c in enumerate(s):
            while c in cnt:
                cnt.remove(s[left])
                left += 1
            cnt.add(c)

            ans = max(ans, right - left + 1)
        return ans

if __name__ == "__main__":
    solution = Solution()
    s = 'abcabcbb'
    result = solution.lengthOfLongestSubstring(s)
    print(result)