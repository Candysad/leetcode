#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#
from functools import cache
# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(stat, i):
            if i == n + 1: return 1
            
            t = 0
            for j in range(1, n+1):
                if (i % j == 0 or j % i == 0) and (1 << j) & stat == 0:
                    t += dfs(stat | (1 << j), i + 1)
            return t
        return dfs(0, 1)    
# @lc code=end