#
# @lc app=leetcode.cn id=163 lang=python3
#
# [163] 缺失的区间
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        left = lower
        p = 0
        n = len(nums)
        result = []
        while p < n:
            if left == nums[p]:
                left = nums[p] + 1
            
            else:
                result.append([left, nums[p]-1])
                left = nums[p] + 1
            p += 1
        if left <= upper:
            result.append([left, upper])
        return result  
# @lc code=end