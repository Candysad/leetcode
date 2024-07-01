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
        def dfs(i, free):
            if free >= n - i: return 0
            if i == n:
                return inf
            
            return min(dfs(i+1, free + time[i]) + cost[i], dfs(i+1, free - 1))
        
        return dfs(0, 0)
# @lc code=end