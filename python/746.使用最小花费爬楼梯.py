#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0, dp1 = 0, 0
        for i in range(2, len(cost) + 1):
            dp0, dp1 = dp1, min(dp0 + cost[i-2], dp1 + cost[i-1])
        return dp1    
# @lc code=end