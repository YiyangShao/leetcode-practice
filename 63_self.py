class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mem = [[0 for i in range(n)]for i in range(m)]
        for i in range(n):
            mem[0][i] = 1
            if obstacleGrid[0][i] == 1:
                    mem[0][i] = 0
                    break
        for i in range(m):
            mem[i][0] = 1
            if obstacleGrid[i][0] == 1:
                    mem[i][0] = 0
                    break
        
        for i in range(1,m):
            for j in range(1,n):
                mem[i][j] = mem[i-1][j] + mem[i][j-1]
                if obstacleGrid[i][j] == 1:
                    mem[i][j] = 0
        print(mem)
        return mem[-1][-1]