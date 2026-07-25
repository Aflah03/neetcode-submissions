class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(curr,ans,i):
            if curr ==target:
                res.append(ans[:])
                return True
            if curr > target:
                return False
            for i in range(i, len(nums)):
                ans.append(nums[i])
                # print(ans)
                dfs(curr+nums[i],ans,i)
                ans.pop()
        ans = []
        dfs(0,ans,0)
        return res
        