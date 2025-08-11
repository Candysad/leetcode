#
# @lc app=leetcode.cn id=2915 lang=python3
#
# [2915] 和为目标值的最长子序列的长度
#

# @lc code=start
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        
        nums.sort()
        for coin in nums:
            if coin > target: break
            for i in range(target, 0, -1):
                if i >= coin and dp[i-coin] > 0:
                    dp[i] = max(dp[i-coin] + 1, dp[i])
        return dp[-1] - 1
# @lc code=end