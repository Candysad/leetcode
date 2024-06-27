#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from math import inf
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        正数会变大
        负数会变小
        dp[i] 表示到当前位置的最大和
        前面dp[i-1]是负数那自己就是最大的
        前面不是负数说明前面可以加到i
        '''       
        result = nums[0]
        pre = nums[0]
        for num in nums[1:]:
            if pre >= 0:
                pre += num
            else:
                pre = num
            result = max(result, pre)
        return max(result, pre)
# @lc code=end