#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        @cache
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return max(1-dungeon[i][j], 1)
            
            t1 = inf
            if i < m-1:
                t1 = dfs(i+1, j)
            
            t2 = inf
            if j < n-1:
                t2 = dfs(i, j+1)
            
            t = min(t1, t2)
            # now + d[i][j] >= t
            return max(t-dungeon[i][j], 1)
        
        return dfs(0, 0)
# @lc code=end