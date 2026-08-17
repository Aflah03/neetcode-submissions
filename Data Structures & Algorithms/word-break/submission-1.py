class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for word in wordDict:
                if word == s[i:i+len(word)]:
                    if dfs(i+len(word)):
                        dp[i] =True
                        return dp[i]
                
            dp[i] =False
            return dp[i]
        return dfs(0)
