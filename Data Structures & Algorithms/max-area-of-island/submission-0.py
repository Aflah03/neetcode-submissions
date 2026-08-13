class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        M = len(grid)
        N = len(grid[0])
        res = 0
        ans = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(i,j):
            nonlocal ans
            nonlocal res
            res +=1
            ans = max(res, ans)
            # print("in dfs and i, j are : ", i , j)
            for x,y in directions:
                r = i + x
                c = j + y
                if r >=0 and c >=0 and r < M and c < N and grid[r][c] == 1 and  (r,c) not in seen:
                    seen.add((r,c))
                    dfs(r,c)    
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (i,j) not in seen:
                    seen.add((i,j))
                    res = 0
                    # print("DFS CALLED AT : ", i, j)
                    dfs(i,j)
        return ans