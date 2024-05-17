#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        '''
        标准二维动态规划
        '''
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1] + (1 if text1[i-1] == text2[j-1] else 0)
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        
        
        '''
        优化二维数组变成一维
        '''
        # len1 = len(text1)
        # len2 = len(text2)
        # dp = [0 for _ in range(len2+1)]
        
        # for i in range(1, len1 + 1):
        #     last= dp[0]
        #     for j in range(1, len2 + 1):
        #         now = dp[j]
        #         if text1[i-1] == text2[j-1]:
        #             dp[j] = last + 1
        #         else:
        #             dp[j] = max(dp[j], dp[j-1])
        #         last = now
        
        # return dp[-1]
        
# @lc code=end

