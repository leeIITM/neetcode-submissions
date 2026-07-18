class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def f(ind,l = []):
            
            if ind > len(nums):
                return
            if ind == len(nums):
                out.append(l[:])
                return
            # pick 
            #l.append(nums[ind])
            f(ind + 1, l + [nums[ind]])
            # not pick
        
            f(ind + 1, l)
        f(0,[])
        return out

