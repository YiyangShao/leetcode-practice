class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        p = 0
        while p < l-1:
            a = nums[p]
            if p+a>= l-1:
                return True
            if a == 0:
                return False
            m = 0
            s = 0
            for i in range(1,a+1):
                if i+nums[p+i] > m:
                    s = i
                    m = i+nums[p+i]
            p = p+s
        return True