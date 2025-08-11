#
# @lc app=leetcode.cn id=1553 lang=python3
#
# [1553] 吃掉 N 个橘子的最少天数
#
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def minDays(self, n: int) -> int:
        
        @cache
        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            
            t1 = dfs(i//2) + i % 2
            t2 = dfs(i//3) + i % 3

            return min(t1, t2) + 1
        
        return dfs(n)
# @lc code=end

