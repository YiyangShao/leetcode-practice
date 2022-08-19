class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        c = 0
        while s and s[-1] == " ":
            s = s[:-1]
        while s and s[-1] != " ":
            c += 1
            s = s[:-1]
        return c