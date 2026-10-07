class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        ans = 0
        i = 0
        for j in range(len(s)):
            if s[j] in char_map:
                i = max(i, char_map[s[j]] + 1)
            char_map[s[j]] = j
            ans = max(ans, j - i + 1)
        return ans
