class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])
        q = deque()
        for i in range (0,r):
            for j in range(0,c):
                if grid[i][j] == 0:
                    q.append([i,j])
        level = 1
        directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
        while(len(q) > 0):
            s = len(q)
            for i in range(0,s):
                rr, cc = q.popleft()
                for first,second in directions:
                    rval = rr+ first
                    cval = cc + second
                    if rval>=0 and cval>=0 and rval< r and cval < c and grid[rval][cval] == 2147483647:
                        grid[rval][cval] = level
                        q.append([rval,cval])
            level = level+1 
            