class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacle = []
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacle.append((i,j))
        #print(dp)
        dp[0][0]=0
        for i in range(0,m):
            for j in range(0,n):
                if (i,j) in obstacle:
                    dp[i][j] = 0
                else:
                    if i == 0  and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]
        