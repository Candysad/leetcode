#
# @lc app=leetcode.cn id=256 lang=python3
#
# [256] 粉刷房子
#

# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        dp = [0, 0, 0]
        for i in range(n):
            t0 = min(dp[1], dp[2]) + costs[i][0]
            t1 = min(dp[0], dp[2]) + costs[i][1]
            t2 = min(dp[0], dp[1]) + costs[i][2]
            dp[0], dp[1], dp[2] = t0, t1, t2
        
        return min(dp)
# @lc code=end