#
# @lc app=leetcode.cn id=3040 lang=python3
#
# [3040] 相同分数的最大操作数目 II
#
from functools import cache
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        '''
        DFS cache
        '''
        @cache
        def dfs(l, r, target):
            if l >= r: return 0
            
            t = 0
            if nums[l] + nums[l+1] == target:
                t = max(t, dfs(l+2, r, target) + 1)
            
            if nums[r] + nums[r-1] == target:
                t = max(t, dfs(l, r-2, target) + 1)
            
            if nums[l] + nums[r] == target:
                t = max(t, dfs(l+1, r-1, target) + 1)
            
            return t
        
        n = len(nums)
        targets = set([nums[0] + nums[n-1], nums[0] + nums[1], nums[-1] + nums[-2]])
        return max([dfs(0, n-1, target) for target in targets])
# @lc code=end