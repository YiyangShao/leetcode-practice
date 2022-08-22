class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for r in matrix:
            lst = lst + r
        return self.binary_search(lst, target)
    
    
    def binary_search(self,lst,target):
        if len(lst) == 0:
            return False
        if len(lst) == 1:
            return lst[0] == target
        l = len(lst)
        p = lst[l//2]
        if p == target:
            return True
        if p > target:
            return self.binary_search(lst[:l//2],target)
        return self.binary_search(lst[l//2:],target)