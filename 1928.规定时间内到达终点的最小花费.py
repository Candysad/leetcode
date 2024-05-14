#
# @lc app=leetcode.cn id=1928 lang=python3
#
# [1928] 规定时间内到达终点的最小花费
#
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        g = [{} for _ in range(n)]
        
        for node1, node2, time in edges:
            t = g[node1].get(node2, inf)
            g[node1][node2] = min(t, time)
            
            t = g[node2].get(node1, inf)
            g[node2][node1] = min(t, time)
            
        @cache
        def dfs(i, k):
            if k < 0:
                return inf
            if i == n-1 and k >= 0:
                return passingFees[-1]

            t = inf
            p = passingFees[i]
            for j in g[i]:
                w = g[i][j]
                t = min(t, dfs(j, k-w))
            return t + p
        
        result = dfs(0, maxTime)
        return result if result != inf else -1
# @lc code=end

