class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) <  target :
            return 0
        if target < max(nums):
            return 1
        i = 0
        j = 0
        min_len = len(nums)
        summ = nums[i]  
        while i < len(nums)   and j < len(nums)  :
            print(min_len)
            if summ >= target:
                summ -= nums[i]
                min_len = min(min_len , j - i + 1)
                i += 1
            else:
                if j == len(nums) - 1:
                    break
                else:
                    j+=1
                    summ += nums[j]
        return min_len
                