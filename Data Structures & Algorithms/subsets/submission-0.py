class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i,arr):
            res.append(arr.copy())
            if i == len(nums):
                return 
            
            for i in range(i,len(nums)):
                arr.append(nums[i])
                dfs(i+1,arr)
                arr.pop()
        arr = []
        dfs(0,arr)
        return res