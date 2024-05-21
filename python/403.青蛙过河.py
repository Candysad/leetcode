#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#
from functools import cache
# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        target = stones[-1]
        step1 = stones[1]
        stones = set(stones)
        
        @cache
        def dfs(i, k):
            if i not in stones:
                return False
            
            if i == target:
                return True
            
            if k > 1:
                return dfs(i+k-1, k-1) | dfs(i+k, k) | dfs(i+k+1, k+1)
            else:
                return dfs(i+k, k) | dfs(i+k+1, k+1)
        
        return dfs(step1, 1)
# @lc code=end

