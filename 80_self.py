class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        pointer = 1
        m = nums[0]
        counter = 1
        while pointer <= length-1:
            if nums[pointer] == m:
                counter += 1
                if counter > 2:
                    nums.remove(m)
                    nums.append("_")
                    counter -= 1
                    length -= 1
                    pointer -= 1
            else:
                m = nums[pointer]
                counter = 1
            pointer += 1
        return length