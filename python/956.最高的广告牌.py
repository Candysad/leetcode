#
# @lc app=leetcode.cn id=956 lang=python3
#
# [956] 最高的广告牌
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        @cache
        def dfs(i, pre):
            if i == n:
                if pre == 0: return 0
                else: return -inf
            
            return max(
                dfs(i+1, pre), # 不选
                dfs(i+1, pre+rods[i]) + rods[i], # 选第一组
                dfs(i+1, pre-rods[i])  # 选第二组
            )
            
        return dfs(0, 0)
# @lc code=end