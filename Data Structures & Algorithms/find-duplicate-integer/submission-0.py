class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i,num in enumerate(nums):
            if num in seen:
                return num
            seen.add(num)
        return 0 