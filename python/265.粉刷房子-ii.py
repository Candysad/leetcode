#
# @lc app=leetcode.cn id=265 lang=python3
#
# [265] 粉刷房子 II
#
from heapq import *
# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        
        dp = [0] * k
        for i in range(n):
            t = dp.copy()
            heapify(t)
            
            tdp = [0] * k
            for j in range(k):
                predp = t.copy()
                if predp[0] == dp[j]:
                    heappop(predp)
                
                tdp[j] = predp[0] + costs[i][j]
            dp = tdp
        
        return min(dp)
# @lc code=end