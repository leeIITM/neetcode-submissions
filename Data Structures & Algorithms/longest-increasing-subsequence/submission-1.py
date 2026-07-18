class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        i = 1
        while i < len(nums):
            j = i - 1
            while j >-1:
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])  
                    j-=1                  
                else:
                    j -=1
            i +=1
        return max(dp)

        