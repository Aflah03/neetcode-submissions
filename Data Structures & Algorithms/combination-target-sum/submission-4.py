class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr, i, ans):
            if curr > target:
                return
            elif curr == target:
                res.append(ans.copy())
            for i in range(i, len(nums)):
                ans.append(nums[i])
                dfs(curr+ nums[i],i, ans)
                ans.pop()
        dfs(0, 0, [])
        return res