class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Memoization
        n = len(nums)
        i = 0 
        d = {}
        def f(ind,summ):
            if ind == n:
                if summ == target:
                    return 1
                else:
                    return 0
        
            
            # Add
            if (ind+1, summ + nums[ind]) in d:
                add = d[(ind+1, summ + nums[ind])]
            else:
                add = f(ind + 1, summ + nums[ind])
                d[(ind + 1, summ + nums[ind])] = add
            # Subtract
            if (ind +1 , summ - nums[ind]) in d:
                sub = d[(ind +1 , summ - nums[ind])]
            else:
                sub = f(ind + 1 , summ - nums[ind])
                d[(ind +1 , summ - nums[ind])] = sub

            return add  + sub
        
        ans = f(0,0)
        return ans
        


