#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        dp = [True] + [False] * target
        # nums.sort()
        for coin in nums:
            # 01 背包，倒着放避免自己影响自己
            for i in range(target, coin-1, -1):
                dp[i] |= dp[i-coin]
            print(dp)
        
        return dp[-1]
                
        
# @lc code=end

