class Solution:
    def rob(self, nums: List[int]) -> int:
        # Can make it more efficient if i do something with max
        n =  len(nums)
        dp = [0 for i in range(n)]
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            dp[0] = nums[0]
            dp[1] = nums[1]
            i = 2
            max_dp = dp[0]
            while  i< n:
                dp[i] = max(dp[i-1] ,max_dp + nums[i])
                
                if dp[i-1] > max_dp:
                    max_dp = dp[i-1]
                i+=1
            return dp[-1]        