class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        
        dp = [[False] * (len_s + 1) for _ in range(len_p + 1)]
        
        dp[0][0] = True  # Empty pattern matches empty string
        
        # Handling patterns like 'a*', 'b*', 'c*', etc. where '*' matches zero times
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]
        
        for i in range(1, len_p + 1):
            for j in range(1, len_s + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 2][j]  # Zero occurrence of the preceding character
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] |= dp[i][j - 1]  # One or more occurrences of the preceding character
        
        return dp[len_p][len_s]