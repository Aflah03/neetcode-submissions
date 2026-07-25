class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M,N = len(board) , len(board[0])
        def dfs(r,c,k, visit):
            if k == len(word):
                return True
            if(r < 0 or c < 0 or r >=M or c >=N or (r,c) in visit or board[r][c] != word[k]):
                return False
            visit.add((r,c))
             
            res = (dfs(r+1,c,k+1,visit) or dfs(r,c+1,k+1,visit) or dfs(r-1,c,k+1,visit) or dfs(r,c-1,k+1,visit))
            if (res):
                return True
            
            visit.remove((r,c))

        
        for i in range(M):
            for j in range(N):
                if(board[i][j] == word[0]):
                    if(dfs(i,j,0, set())):
                        return True
        return False
                