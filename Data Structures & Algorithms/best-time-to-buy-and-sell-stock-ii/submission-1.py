class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j <= i:
                    dp[i][j] = 0
                else:
                    if prices[j] - prices[i] >=0:
                        if j +1 < n:

                            dp[i][j] = prices[j] - prices[i] + max(dp[j+1])
                        else:
                            dp[i][j] = prices[j] - prices[i]
                    else:
                        if  j + 1 < n:
                            dp[i][j] = max(dp[j])
                        else:
                            dp[i][j] = 0
        out = max(max(sublist) for sublist in dp)
        return out
                    

