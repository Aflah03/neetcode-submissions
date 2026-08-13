class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        mp = {}
        l=0
        res = 0
        for r in range(len(s)):
            mp[s[r]] = 1+mp.get(s[r], 0)
            max_freq = max(max_freq, mp[s[r]])
            if (r-l+1) - max_freq  > k:
                mp[s[l]]-=1
                l+=1
               
            else:
                res = max(res, (r-l+1))
        return res