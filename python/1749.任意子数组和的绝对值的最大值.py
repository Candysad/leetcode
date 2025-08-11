#
# @lc app=leetcode.cn id=1749 lang=python3
#
# [1749] 任意子数组和的绝对值的最大值
#

# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        resultp = nums[0]
        prep = nums[0]
        resultn = nums[0]
        pren = nums[0]
        
        for num in nums[1:]:
            if prep >= 0:
                prep += num
            else:
                prep = num
            resultp = max(resultp, prep)

            if pren <= 0:
                pren += num
            else:
                pren = num
            resultn = min(resultn, pren)
        
        return max(resultp, abs(resultn))
# @lc code=end