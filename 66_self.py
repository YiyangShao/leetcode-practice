class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        l = len(digits)
        p = l-1
        while digits[p] == 10:
            digits[p] = 0
            if p == 0:
                digits.insert(0,1)
                break
            digits[p-1] += 1
            p -= 1
        return digits
            
                