#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        dp[i][j] 表示子串[i...j]成为回文要添加的最少次数
        s[i] == s[j] 
        则dp[i][j] = dp[i+1][j-1]
        有没有可能加一个反而更小？
        
        s[i] != s[j] 则要么一边不动另一边加一个，要么中间不动两边都加，选最小的
        '''
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n+1, 0, -1):
            for j in range(i+1, n+1):
                dp[i][j] = min(
                    dp[i+1][j-1] if s[i-1] == s[j-1] else dp[i+1][j-1] + 2,
                    dp[i+1][j] + 1,
                    dp[i][j-1] + 1
                )
        
        return dp[1][-1]
        
        
# @lc code=end

