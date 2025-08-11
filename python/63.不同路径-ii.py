#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        if g[0][0] == 1: return 0       
        m, n = len(g), len(g[0])
        
        dp = [1] + [0] * (n-1)
        for i in range(m):
            if g[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if g[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]
        return dp[-1]
# @lc code=end

