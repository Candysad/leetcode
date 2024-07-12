#
# @lc app=leetcode.cn id=2970 lang=python3
#
# [2970] 统计移除递增子数组的数目 I
#
from functools import cache
from itertools import pairwise
# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        alls = [b-a > 0 for a,b in pairwise(nums)]
        n = len(nums)
        @cache
        def dfs(i, s, pre):
            if i == n: return 1
            if s == 2:
                if nums[i] <= pre:
                    return 0
                else:
                    return dfs(i+1, 2, nums[i])

            elif s == 1:
                if nums[i] <= pre:
                    return dfs(i+1, 1, pre)
                else:
                    return dfs(i+1, 1, pre) + dfs(i+1, 2, nums[i])

            elif s == 0:
                if nums[i] <= pre:
                    return dfs(i+1, 1, pre)
                else:
                    return dfs(i+1, 1, pre) + dfs(i+1, 0, nums[i])
        
        result = dfs(0,0,0)
        return result - 1 if all(alls) else result 
# @lc code=end