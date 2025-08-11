#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        逆向思维
        两头的 1 是最早出现的
        '''
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i+1, n):
                for mid in range(i+1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[mid] * nums[j] + dp[i][mid] + dp[mid][j])
        
        return dp[0][-1]
# @lc code=end

