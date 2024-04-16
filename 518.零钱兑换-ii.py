#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        完全背包
        以余额从小到大维护数组会使得硬币组合出现重复
        比如 3 会由 1 + 2 和 2 + 1 组合，因为硬币是反复选的会有前后顺序
        
        以硬币面值从小到大维护，可以确定小面值一定先出现，从而避免重复组合
        '''
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[-1]
# @lc code=end

