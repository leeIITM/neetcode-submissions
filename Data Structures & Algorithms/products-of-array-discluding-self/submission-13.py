class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix Suffix Approach
        # Prefic = Product of all elements left of i th index
        # Suffix = Product of all elements right of i th index
        # Prod[i] = Prefix[i] * Suffix[i]
        n = len(nums)
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        prefix[0] = 1
        suffix[n-1] = 1
        res = [1 for i in range(n)]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res
        
            