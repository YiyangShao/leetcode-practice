class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 1
        p1 = 0
        p2 = 0
        l1 = len(matrix)
        l2 = len(matrix[0])
        s = l1*l2
        res = [matrix[0][0]]
        passed = [(0,0)]
        if l2 == 1:
            direction = 2
        for i in range(s-1):
            if direction == 1:
                p2 += 1
                res.append(matrix[p1][p2])
                passed.append((p1,p2))
                if p2 == l2-1 or (p1,p2+1) in passed:
                    direction = 2
                continue
            if direction == 2 and p1 != l1-1:
                p1 += 1
                res.append(matrix[p1][p2])
                passed.append((p1,p2))
                if p1 == l1-1 or (p1+1,p2) in passed:
                    direction = 3
                continue
            if direction == 3:
                p2 -= 1
                res.append(matrix[p1][p2])
                passed.append((p1,p2))
                if p2 == 0 or (p1,p2-1) in passed:
                    direction = 4
                continue
            if direction == 4:
                p1 -= 1
                res.append(matrix[p1][p2])
                passed.append((p1,p2))
                if p1 == 0 or (p1-1,p2) in passed:
                    direction = 1
                continue
        return res
                    
        