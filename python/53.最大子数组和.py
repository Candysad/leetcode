#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from math import inf
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if pre >= 0:
                pre += num
            else:
                pre = num
            result = max(result, pre)
        
        return result
# @lc code=end