class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0 for i in range(n)] for i in range(n)]
        
        d = 1
        p = [0,0]
        m[0][0] = 1
        for i in range(n*n-1):
            if d == 1:
                p[1] += 1
                m[p[0]][p[1]] = i+2
                if p[1] == n-1 or m[p[0]][p[1]+1] != 0:
                    d = 2
                    continue
            if d == 2:
                p[0] += 1
                m[p[0]][p[1]] = i+2
                if p[0] == n-1 or m[p[0]+1][p[1]] != 0:
                    d = 3
                    continue
            if d == 3:
                p[1] -= 1
                m[p[0]][p[1]] = i+2
                if p[1] == n-1 or m[p[0]][p[1]-1] != 0:
                    d = 4
                    continue
            if d == 4:
                p[0] -= 1
                m[p[0]][p[1]] = i+2
                if p[1] == n-1 or m[p[0]-1][p[1]] != 0:
                    d = 1
                    continue
                
        return m 