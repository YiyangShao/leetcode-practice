class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        pos = 0
        step = 0
        while pos <= l:
            a = nums[pos]
            if pos + a >= l-1:
                return step +1
            m = 0
            m1 = 0
            for i in range(a):
                if (i+1) + nums[pos+i+1] > m:
                    m = (i+1) + nums[pos+i+1]
                    m1 = i+1
            pos = pos + m1
            step += 1
        return step
            
            
        