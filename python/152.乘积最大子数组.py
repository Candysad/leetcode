#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from math import inf
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # dp0 最大值
        # dp1 最小值
        # 包含第i个的最大最小值，最大值尽量是正的，最小值尽量是负的
        dp0 = [0] * n
        dp1 = [0] * n
        dp0[0], dp1[0] = nums[0], nums[0]
        
        for i in range(1, n):
            # 顺便把正负也都考虑进去了
            dp0[i] = max(nums[i], nums[i] * dp0[i-1], nums[i] * dp1[i-1])
            dp1[i] = min(nums[i], nums[i] * dp0[i-1], nums[i] * dp1[i-1])
        
        return max(dp0)
# @lc code=end

