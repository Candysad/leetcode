#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2: return False
        
        target = _sum // 2
        
        dp = [1] + [0] * target
        nums.sort()
        
        for coin in nums:
            if coin > target: break
            for i in range(target, coin-1, -1):
                dp[i] |= dp[i-coin]
        
        return dp[-1] == 1
# @lc code=end

