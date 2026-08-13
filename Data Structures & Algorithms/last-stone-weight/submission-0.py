class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for num in stones:
            heapq.heappush(maxHeap, -1 * num)
        while len(maxHeap) > 1:
            y = -1* heapq.heappop(maxHeap)
            x = -1 * heapq.heappop(maxHeap)
            if y-x > 0:
                heapq.heappush(maxHeap, -1*(y-x))
        return -1*maxHeap[0] if maxHeap else 0