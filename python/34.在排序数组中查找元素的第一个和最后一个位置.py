#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from bisect import bisect_left, bisect_right
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = bisect_left(nums, target)
        if i == n or nums[i] != target:
            return [-1, -1]
        
        j = bisect_right(nums, target) - 1
        return[i, j]
# @lc code=end

