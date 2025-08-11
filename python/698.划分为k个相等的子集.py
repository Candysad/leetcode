#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from collections import defaultdict
from functools import cache
# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        _sum = sum(nums)
        if _sum % k: return False
        target = _sum // k
        
        nums.sort()
        @cache
        def dfs(stat, pre):
            if stat == (1 << n) - 1: return True
            for i in range(n):
                if pre + nums[i] > target: break
                
                if (stat >> i) & 1 == 0:
                    now = pre + nums[i] % target
                    if dfs(stat | (1 << i),  now):
                        return True
            
            return False
        
        return dfs(0, 0)
# @lc code=end