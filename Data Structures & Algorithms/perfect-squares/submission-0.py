class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1,len(dp)):
            for j in range(1,i+1):
                s = j * j
                if i < s:
                    break
                dp[i] = min(dp[i] , dp[i - s] + 1)
        return dp[n]