#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        @cache
        def dfs(pre, i):
            if i == n:
                if pre >= 0: return pre
                else: return inf # 负的不要
            
            return min(dfs(pre+stones[i], i+1), dfs(pre-stones[i], i+1))

        return dfs(0, 0)
# @lc code=end