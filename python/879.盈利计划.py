#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#
from functools import cache
# @lc code=start
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dfs(i, np, p):
            if np == n:
                if p >= minProfit: return 1
                else: return 0
            
            return dfs(i+1, np+group[i], min(minProfit, p+profit[i])) + dfs(i+1, np, p)
        
        return dfs(0, 0, 0)    
# @lc code=end