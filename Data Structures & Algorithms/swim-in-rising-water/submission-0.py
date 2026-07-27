class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        minHeap = []
        neighbours =[[0,1],  [1,0],[-1,0], [0,-1]]
        res = 0
        q = deque()
        visit = set()
        minHeap.append((grid[0][0],0,0))
        while minHeap:
            print("in the while loop")
            val, x,y = heapq.heappop(minHeap)
            res = max(res, val)
            if x == m-1 and y == n-1:
                return res
            visit.add((x,y))
            for rr, cc in neighbours:
                r = rr+ x
                c = cc + y
                if r >=0 and r <m and c >= 0 and c < n and (r,c) not in visit:
                    heapq.heappush(minHeap, (grid[r][c], r ,c ))
        return res