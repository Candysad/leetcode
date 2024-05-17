#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        一种状态
        '''
        # n = len(nums)
        # dp = [0] * (n + 1)
        # dp[1] = nums[0]
        # for i in range(2, n+1):
        #     dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        # return dp[-1]
        
        '''
        代码简化
        易读性差
        '''
        n = len(nums)
        left, right = 0, nums[0]
        
        for i in range(1, n):
            left, right = right, max(left + nums[i], right)
        return right
        
        '''
        两种状态dp
        '''
        # n = len(nums)
        # dp0 = [0] * (n + 1) # 今天不偷
        # dp1 = [0] * (n + 1) # 今天偷

        # for i in range(1, n+1):
        #     dp0[i] = max(dp0[i-1], dp1[i-1])
        #     dp1[i] = dp0[i-1] + nums[i-1]
        
        # return max(dp0[-1], dp1[-1])
# @lc code=end

