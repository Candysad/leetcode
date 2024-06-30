#
# @lc app=leetcode.cn id=2742 lang=python3
#
# [2742] 给墙壁刷油漆
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dfs(i, pret):
            if pret >= n-i: return 0
            if i == n:
                if pret >= 0: return 0
                else: return inf
            
            c = cost[i]
            t = time[i]
            
            return min(dfs(i+1, pret-1), dfs(i+1, pret+t) + c)
            
        return dfs(0, 0)
# @lc code=end