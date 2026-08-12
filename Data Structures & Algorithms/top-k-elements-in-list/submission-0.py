class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        mp = defaultdict(int)
        for num in nums:
            mp[num] +=1
        for item, freq in mp.items():
            minHeap.append((freq, item))
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        res = []
        for freq, item in minHeap:
            res.append(item)
        return res