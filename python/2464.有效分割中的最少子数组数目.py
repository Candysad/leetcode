#
# @lc app=leetcode.cn id=2464 lang=python3
#
# [2464] 有效分割中的最少子数组数目
#
from functools import cache
from math import gcd, inf
# @lc code=start
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, last):
            if i == n-1:
                if gcd(last, nums[i]) > 1:
                    return 1
                else:
                    return inf
            
            t = dfs(i+1, last)
            if gcd(last, nums[i]) > 1:
                t = min(t, 1 + dfs(i+1, nums[i+1]))
            return t

        result = dfs(0, nums[0])
        return result if result != inf else -1    
# @lc code=end

