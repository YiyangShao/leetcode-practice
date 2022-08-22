class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        m1 = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    m1[i][j] = 1
        for i in range(m):
            for j in range(n):
                if m1[i][j] == 1:
                    for p in range(m):
                        matrix[p][j] = 0
                    for p in range(n):
                        matrix[i][p] = 0
                
                    