#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        子序列，不用在原字符串里连续
        可以跳过其他字符，所以只需要看最长长度+新增加的部分
        动态规划
        保留i 和 j 之间最长回文序列的长度
        '''
        n = len(s)
        dp = [[0]*n for i in range(n)]
        
        for i in range(n-1, -1, -1): # i 在前面
            dp[i][i] = 1
            for j in range(i+1, n): # j 在后面
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2# 两头相同，增加两个字
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) #两头不同，取当前里面最长的
        return dp[0][-1] # 开头结尾组成的状态就是全部里面最长的  
# @lc code=end


