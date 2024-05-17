#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:  
        for i in range(2, len(cost)):
            cost[i] = cost[i] + cost[i-1] if cost[i-1] < cost[i-2] else cost[i] + cost[i-2]
        print(cost)
        return cost[-2] if cost[-2] < cost[-1] else cost[-1]
# @lc code=end

