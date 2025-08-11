#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # 开头结尾不能同时选，那就分开考虑
        # 一定选开头
        dp0t, dp0b = nums[0], 0
        # 一定不选开头
        dp1t, dp1b = 0, 0
        
        for num in nums[1:]:
            t0 = dp0b + num
            b0 = max(dp0t, dp0b)
            dp0t, dp0b = t0, b0
            
            t1 = dp1b + num
            b1 = max(dp1t, dp1b)
            dp1t, dp1b = t1, b1
        
        # 一定选开头的，则结尾一定不选
        return max(dp0b, dp1b, dp1t)
# @lc code=end