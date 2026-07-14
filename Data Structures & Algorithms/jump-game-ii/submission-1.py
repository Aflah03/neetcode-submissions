class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(nums)-1:
                return 0
            if nums[i] == 0:
                return float('inf')
            res = float('inf')
            start = i+1

            end = min(len(nums) -1 , i+nums[i])
            for j in range(start, end+1):
                val =1+ dfs(j)
                res = min(res,val)
            dp[i] = res
            return res
        return dfs(0)   
            