class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        l = 0
        arr = [-1] * 128
        res = 0
        for r in range(len(s)):
            idx = ord(s[r]) -ord('a')
            if arr[idx] != -1:
                l = max(l, arr[idx]+1)
            arr[idx] = r
            res = max(res, r-l+1)
        return res