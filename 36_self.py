class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            l = [k for k in board[i]]
            while "." in  l:
                l.remove(".")
            s = set(l)
            if len(l) != len(s):
                return False
                    
        for j in range(9):
            l = [board[i][j] for i in range(9)]
            while "." in  l:
                l.remove(".")
            s = set(l)
            if len(l) != len(s):
                return False
                    
        for i in [[0,1,2],[3,4,5],[6,7,8]]:
            for j in [[0,1,2],[3,4,5],[6,7,8]]:
                l = []
                for ni in i:
                    for nj in j:
                        l.append(board[ni][nj])
                while "." in  l:
                    l.remove(".")
                s = set(l)
                if len(l) != len(s):
                    return False
        return True
