class Solution:
    def checkValidString(self, s: str) -> bool:
        curr = 0
        dp = {}
        def dfs(curr, i):
            if (curr,i) in dp:
                return dp[(curr,i)]
            if curr< 0:
                return False
            if i >= len(s):
                return curr == 0

            if s[i] == '(':
                res = dfs(curr+1, i+1)
            if s[i] == ')':
                res = dfs(curr-1, i+1)
            if s[i] == '*':
                res =  dfs(curr+1, i+1) or dfs(curr-1, i+1) or dfs(curr, i+1)
            dp[(curr,i)] = res
            return res
        return dfs(0,0)
            