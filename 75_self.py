class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[p],nums[i] = nums[i],nums[p]
                p += 1
        for i in range(p,n):
            if nums[i] == 1:
                nums[p],nums[i] = nums[i],nums[p]
                p += 1
            