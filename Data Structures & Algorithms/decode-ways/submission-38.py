class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] represents the number of ways to decode s[i:]
        dp = [0] * (n + 1)
        
        # Base case: empty string has one way to be decoded
        dp[n] = 1
        
        # Iterate backwards
        for i in range(n - 1, -1, -1):
            # If current char is '0', it cannot start a valid decoding
            if s[i] == '0':
                dp[i] = 0
            else:
                # Option 1: Take single digit
                dp[i] = dp[i + 1]
                
                # Option 2: Take two digits if valid (10-26)
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    dp[i] += dp[i + 2]
                    
        return dp[0]
            