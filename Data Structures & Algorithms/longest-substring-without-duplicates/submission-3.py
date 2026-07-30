class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = [-1]*128

        l = 0
        ans = 0
        for r in range(len(s)):
            idx = ord(s[r])-ord('a')
            if(mp[idx]!= -1):
                l = max(l, mp[idx] +1)
            mp[idx] = r
            ans = max(ans, r-l+1)
        return ans