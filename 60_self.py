class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l = [i+1 for i in range(n)]
        res = ""
        k -= 1
        for i in range(n):
            p = 0
            while k >= self.fact(n-i-1):
                k -= self.fact(n-i-1)
                p += 1
            res = res + str(l[p])
            l.pop(p)
        return res
        
        
        
    def fact(self,n):
        s = 1
        for i in range(1,n+1):
            s *= i
        return s