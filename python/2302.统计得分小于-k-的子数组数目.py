#
# @lc app=leetcode.cn id=2302 lang=python3
#
# [2302] 统计得分小于 K 的子数组数目
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        _sum = 0
        left = 0
        for right in range(n):
            _sum += nums[right]
            while (right - left + 1) * _sum >= k:
                _sum -= nums[left]
                left += 1
            result += right - left + 1
        return result
# @lc code=end