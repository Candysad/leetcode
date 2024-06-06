#
# @lc app=leetcode.cn id=2787 lang=python3
#
# [2787] 将一个数字表示成幂的和的方案数
#

# @lc code=start
class Solution:
    def numberOfWays(self, target: int, x: int) -> int:
        '''
        0-1背包
        '''
        mod = 10**9 + 7
        coins = []
        for i in range(1, target+1):
            if i**x > target: break
            coins.append(i**x)
        
        dp = [1] + [0] * target
        _maxi = target
        for coin in coins:
            for i in range(_maxi, coin-1, -1):
                dp[i] += dp[i-coin]
                dp[i] %= mod
        
        return dp[-1] % mod
# @lc code=end