class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Why rejecting duplicates work? and why is it inherently working?
        out = []
        nums = [i+1 for i in range(n)]
        
        def f(ind, left , l):
            if left == 0:
                out.append(l[:])
            if ind >= len(nums):
                return
            # Pick
            l.append(nums[ind])
            
            f(ind + 1, left - 1 ,l)

            # Not pick
            l.pop()
            f(ind + 1, left , l)
        
        f(0,k,l = [])
        o = []
        for i in out:
            if i not in o:
                o.append(i)
            else:
                pass
        return o