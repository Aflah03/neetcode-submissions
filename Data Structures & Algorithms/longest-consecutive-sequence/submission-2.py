class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set()
        if len(nums) ==0:
            return 0
        for num in nums:
            mp.add(num)
        res = 1
        for num in mp:
            if num-1 in mp:
                continue
            else:
                i=1
                while num+ i in mp:
                    i +=1
                    res = max(res, i)
        return res