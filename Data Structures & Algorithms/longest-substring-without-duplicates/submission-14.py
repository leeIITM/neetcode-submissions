class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = 0
        j = 0
        max_len = 0
        while j <len(s):
            if s[j] not in d or d[s[j]] <i :
                d[s[j]] = j
              
            elif s[j] in d:
                i = d[s[j]] + 1
                d[s[j]] = j
                
            else:
                pass
            print(max_len)
            if max_len < j - i + 1:
                max_len = j - i +1
            j+=1
        return max_len
        