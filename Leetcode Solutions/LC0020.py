class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(s):
            for j in range(1+1,s):
                if (s[i] == s [j]):
                    return True
                else:
                    return False