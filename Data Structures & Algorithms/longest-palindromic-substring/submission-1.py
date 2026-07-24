class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):
            # odd palindrome
            l , r = i , i
        
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -=1
                r +=1
            temp_pal = s[l+1 : r  ]
            
            if len(temp_pal) > len(out):
                out = temp_pal
            
            

            # even palindrome
            l = i
            r = i + 1
            while l>= 0 and r <len(s) and s[l] == s[r]:
                l -=1
                r +=1
            temp_pal = s[l +1 : r  ]
            
            if len(temp_pal) > len(out):
                out = temp_pal

        return out

                