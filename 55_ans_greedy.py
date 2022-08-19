class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)-1
        for i in range(l,-1,-1):
            if i + nums[i] >= l:
                l = i
        return l == 0
        
        
        return True