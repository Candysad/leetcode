#
# @lc app=leetcode.cn id=2369 lang=python3
#
# [2369] 检查数组是否存在有效划分
#
from functools import cache
# @lc code=start
class Solution:
    def validPartition(self, nums: List[int]) -> bool:    
        '''
        dfs
        '''
        @cache
        def dfs(i):
            if i == 0:
                return False
            if i == 1:
                return nums[1] == nums[0]
            if i == 2:
                return (nums[0] == nums[1] == nums[2]) | (nums[0] + 2 == nums[1] + 1 == nums[2])
            
            t2 = dfs(i-2) & (nums[i] == nums[i-1])
            t3 = dfs(i-3) & ((nums[i-2] == nums[i-1] == nums[i]) | (nums[i-2] + 2 == nums[i-1] + 1 == nums[i]))
            return t2 | t3
            
        return dfs(len(nums)-1)
        
        '''
        DP
        '''
        # n = len(nums)
        # if n == 2:
        #     return nums[1] == nums[0]
        # if n == 3:
        #     return (nums[0] == nums[1] == nums[2]) | (nums[0] + 2 == nums[1] + 1 == nums[2])
        
        # dp = [False] * n
        # dp[1] = nums[1] == nums[0]
        # dp[2] = (nums[0] == nums[1] == nums[2]) | (nums[0] + 2 == nums[1] + 1 == nums[2])
        # for i in range(3, n):
        #     dp[i] |= dp[i-2] & (nums[i-1] == nums[i])
        #     dp[i] |= dp[i-3] & ((nums[i-2] == nums[i-1] == nums[i]) | (nums[i-2] + 2 == nums[i-1] + 1 == nums[i]))

        # return dp[-1]
# @lc code=end

