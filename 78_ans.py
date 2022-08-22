class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = 2**n
        res = []
        for i in range(s):
            cur = []
            for j in nums:
                if i % 2:
                    cur.append(j)
                i = i // 2
            res.append(cur)
        return res
            
                