class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = [-1] * 128
        l = 0
        res = 0
        for r in range(len(s)):
            if mp[ord(s[r])] != -1:
                l = max(l, mp[ord(s[r])]+1)
            mp[ord(s[r])] = r
            res= max(res, r-l+1)

        return res