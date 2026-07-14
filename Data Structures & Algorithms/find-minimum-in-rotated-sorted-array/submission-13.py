class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        if len(nums) == 1:
            return nums[0]
        def bin_s(low,high,nums):
            mid = (low + high) // 2
            if nums[mid] < nums[mid -1]:
                min_ele = nums[mid]
                #return nums[mid]
            elif nums[-1] < nums[mid]:
                #if nums[mid] > nums[-1]:
                    low = mid +1
                    min_ele = bin_s(low,high,nums)
                
            else:
                high = mid -1
                min_ele = bin_s(low,high,nums)
            return min_ele
        x = bin_s(0,n-1,nums)
        return x
            
       


        
        