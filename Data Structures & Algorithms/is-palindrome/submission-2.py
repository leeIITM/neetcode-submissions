class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(s)
        l = [i.lower() for i in l]
        print(l)
        p = []
        for i in l:
            if i.isalnum():
                p.append(i)
            
            else:
                pass
        n = len(p)
        i = 0
        j = n - 1
        print(l)
        while i < j:
            if p[i] == p[j]:
                i+=1
                j-=1
            else:
                return False
        return True