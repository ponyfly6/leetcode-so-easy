# len(s.split()[-1])


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        length = 0
        i = n - 1

        # 1 skip the null spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        if i < 0:
            return 0
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length





























