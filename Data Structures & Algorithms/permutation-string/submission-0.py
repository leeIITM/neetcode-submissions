class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        element = sorted(s1)
        n = len(element)
        for i in range(len(s2) - n+1):
            if sorted(s2[i : i + n]) == element:
                return True
        return False
        