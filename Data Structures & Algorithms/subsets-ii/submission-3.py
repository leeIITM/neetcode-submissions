class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        def f(i,l):
            if i >=len(nums):
                out.append(l[ : ])
                return
            # pick
            l.append(nums[i])
            f(i+1,l)

            # not pick
            l.pop()
            f(i+1, l)
        
        f(0,[])
        print(out)
        o = [sorted(i) for i in out]
        p=[]
        for i in o:
            if i not in p:
                p.append(i)
            else:
                pass
        return p
           