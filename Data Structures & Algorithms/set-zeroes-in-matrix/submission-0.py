class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])

        cols = [0]* N
        rows = [0]*M
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    cols[j] =1 
                    rows[i] = 1
        
        for i in range(M):
            for j in range(N):
                if cols[j] ==1 or rows[i] == 1:
                    matrix[i][j] = 0
        