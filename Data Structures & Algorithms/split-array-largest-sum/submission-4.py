class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def cansplit(target):
            cursum = 0
            subarray = 1
            for num in nums:
                cursum += num
                if cursum > target:
                    subarray +=1
                    
                    if subarray > k:

                        return False
                    cursum = num
                        
            return True
        
        low = max(nums)
        high = sum(nums)
        res = high
        while low <= high:
            mid = low + (high - low) // 2
            if cansplit(mid):
                res = mid
                high = mid -1
            else:
                low  = mid + 1
        return res

            
        