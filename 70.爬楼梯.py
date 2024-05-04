#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# @lc code=start

class Solution:
    def __init__(self) -> None:
        '''
        cheat table
        '''
        self.dp = [0, 1, 2] + [0] * 43
        for i in range(3, 46):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
    
    def climbStairs(self, n: int) -> int:
        '''
        动态规划简单题
        '''
        return self.dp[n]
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        '''
        空间优化
        '''
        dp1, dp2 = 1, 2
        for i in range(3, n+1):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2
        
        '''
        打表
        '''
        dp = [0, 1, 2] + [0] * (n - 2)
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
# @lc code=end