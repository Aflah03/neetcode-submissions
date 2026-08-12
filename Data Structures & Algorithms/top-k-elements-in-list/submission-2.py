class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        max_freq = 0
        for num in nums:
            mp[num]+=1
            max_freq = max(mp[num], max_freq)
        print(max_freq)
        res = [[] for i in range(max_freq+1)]
        for item, freq in mp.items():
            res[freq].append(item)
        print(res)
        i = len(res)-1
        ans = []
        while i>=0 and len(ans) < k:
            if res[i]:
                ans.extend(res[i])
            i-=1
        return ans