class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(visit, arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return 
            for i in range(len(nums)):
                if i not in visit:
                    visit.add(i)
                    arr.append(nums[i])
                    dfs(visit,arr)
                    visit.remove(i)
                    arr.pop()
                
        dfs(set(),[])
        return res