#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        if m == 0:
            if n == 0 or p == '*' * n:
                return True
            else:
                return False
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][0] = 1
        
        for i in range(0, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = 1 & dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j-1] | dp[i-1][j] | dp[i][j-1]
        
        return dp[-1][-1] == 1
# @lc code=end

