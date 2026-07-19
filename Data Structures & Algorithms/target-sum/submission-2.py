class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Recursion approach
        n = len(nums)
        i = 0 
        def f(ind,summ):
            if ind == n:
                if summ == target:
                    return 1
                else:
                    return 0
        
            
            # Add
            add = f(ind + 1, summ + nums[ind])
            # Subtract
            sub = f(ind + 1 , summ - nums[ind])

            return add  + sub
        
        ans = f(0,0)
        return ans
        


