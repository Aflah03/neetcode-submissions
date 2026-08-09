class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(N):
            for  j in range(i,N):
                if i==j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for row in matrix:
            row.reverse()
        