class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        p = [len(i) for i in strs]
        mini = min(p)
        for i in range(mini):
            c = 0
            for j in range(1,len(strs)):
                if strs[j-1][i] == strs[j][i]:
                    c+=1
            if c == len(strs) - 1:
                s+=strs[0][i]
            else:
                break
        return s
            

