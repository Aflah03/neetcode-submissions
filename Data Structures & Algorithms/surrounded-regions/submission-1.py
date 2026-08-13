class Solution:
    def solve(self, board: List[List[str]]) -> None:
        t = 0
        r = len(board[0])
        b = len(board)
        l = 0
        m = len(board)
        n = len(board[0])
        edge = set()
        for i in range(l, r):
            if board[t][i] == 'O':
                edge.add((t,i))
        t+=1
        for i in range(t, b):
            if board[i][r-1] == 'O':
                edge.add((i,r-1))
        r-=1
        for i in range(r, l-1 , -1):
            if board[b-1][i] == 'O':
                edge.add((b-1,i))
        b-=1
        for i in range(b, t-1, -1):
            if board[i][l] == 'O':
                edge.add((i,l))
        l+=1
        directions = [[0,1],[1,0], [-1,0],[0,-1]]
        def dfs(i, j):
            if board[i][j] == 'X':
                return
            board[i][j] ="Z"
            for x, y  in directions:
                r = x+i
                c = y + j
                if r >=0 and c >=0 and r < m and c < n and board[r][c]== 'O':
                    board[r][c] = 'Z'
                    dfs(r,c)
        for x, y in edge:
            print("DFS Called at: ", x, y)
            dfs(x,y)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z':
                    board[i][j] = 'O'

