#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = n+1
        left = 0
        _sum = 0
        for right, num in enumerate(nums):
            _sum += num
            while _sum >= target:
                result = min(result, right - left + 1)
                _sum -= nums[left]
                left += 1
        return result if result < n + 1 else 0
# @lc code=end