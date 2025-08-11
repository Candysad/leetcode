#
# @lc app=leetcode.cn id=2435 lang=python3
#
# [2435] 矩阵中和能被 K 整除的路径
#

# @lc code=start
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * k for i in range(n)] for j in range(m)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                num = grid[i][j]
                
                if i < m-1:
                    for t in range(k):
                        dp[i][j][(num + t) % k] += dp[i+1][j][t]
                
                if j < n-1:
                    for t in range(k):
                        dp[i][j][(num + t) % k] += dp[i][j+1][t]
                
        return dp[0][0][0] % mod
# @lc code=end