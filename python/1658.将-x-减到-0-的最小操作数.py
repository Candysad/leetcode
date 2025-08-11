#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        滑窗
        '''
        n = len(nums)
        left, _sum = 0, 0
        result = -1
        
        target = sum(nums) - x
        if target < 0: return -1
        
        for right, num in enumerate(nums):
            _sum += num
            while _sum > target:
                _sum -= nums[left]
                left += 1
                
            if _sum == target:
                result = max(result, right - left + 1)
        return n - result if result != -1 else -1
        
        
        '''
        DFS 爆内存
        '''
        # n = len(nums)
        # _sum = sum(nums)
        # target = _sum - x
        # if target < 0: return -1
        
        # @cache
        # def dfs(res, left, right):
        #     if res == target:
        #         return 0
            
        #     if res < target or left > right:
        #         return inf
            
        #     return min(dfs(res - nums[left], left+1, right), dfs(res - nums[right], left, right-1)) + 1

        # result = dfs(sum(nums), 0, n-1)
        # return result if result != inf else -1
        
# @lc code=end