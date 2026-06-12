class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        nums.sort()
        dp = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] == nums[i]-1:
                    dp[i] = dp[j] + 1
                else:
                    pass
        print(dp)
        return max(dp)