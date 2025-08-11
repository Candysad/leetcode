#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#
from functools import cache
# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dfs(i, steps):
            if i < 0 or i == arrLen: return 0
            if i == steps:
                return 1
            if i > steps:
                return 0

            return (dfs(i, steps-1) + dfs(i-1, steps-1) + dfs(i+1, steps-1)) % mod
        
        return dfs(0, steps) % mod
# @lc code=end