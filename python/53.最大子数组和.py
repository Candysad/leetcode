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
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        
        return max(nums)
        
        
        
        '''
        dp[i] 为从0至i的和
        [i...j] 的和为 dp[j] - dp[i]
        找每个位置和前面最小的之间的差
        '''
        # sums = []
        # s = 0
        # for num in nums:
        #     s += num
        #     sums.append(s)
        
        # _min = 0
        # result = -inf
        # for s in sums:
        #     t = s - _min
        #     result = max(result, t)
        #     _min = min(_min, s)
        
        # return result
        
# @lc code=end

