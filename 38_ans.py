class Solution:
    def countAndSay(self, n: int) -> str:
        def generateNext(cur):
            s, e = 0, 0
            ans = ''
            while(e <= len(cur)):
                if(e == len(cur) or cur[s] != cur[e]):
                    ans += str(e - s) + cur[s]
                    s = e
                e += 1
            return ans
                    
        cur = '1'
        for i in range(2, n+1):
            cur = generateNext(cur)
        return cur 