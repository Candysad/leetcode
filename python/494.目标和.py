#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
from functools import cache
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(pre, i):
            if i == n:
                if pre == target: return 1
                else: return 0
            
            return dfs(pre + nums[i], i+1) + dfs(pre-nums[i], i+1)

        return dfs(0, 0)
# @lc code=end