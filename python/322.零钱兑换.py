#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        位运算
        '''
        dp = 1 << amount
        result = 0
        while dp & 1 == 0:
            t = dp
            for coin in coins:
                dp |= t >> coin
            if t == dp:
                return -1
            result += 1
        return result
        
        '''
        递归
        '''
        # @cache
        # def dfs(s):
        #     if s == amount:
        #         return 0
        #     if s > amount:
        #         return inf

        #     t = inf
        #     for coin in coins:
        #         t = min(t, dfs(s + coin))
            
        #     return t + 1
        # result = dfs(0)
        # return result if result != inf else -1
                
        '''
        动态规划
        '''
        # if amount == 0:
        #     return 0
        # coins.sort()
        
        # dp = [-1] * (amount + 1)
        # dp[0] = 0
        
        # def trans(pre:int, now:int):
        #     if dp[pre] == -1:
        #         return
        #     if dp[now] == -1:
        #         dp[now] = dp[pre] + 1
        #     else:
        #         dp[now] = min(dp[now], dp[pre] + 1)
        
        # for now_amount in range(1, amount + 1):
        #     for coin in coins:
        #         if coin > now_amount:
        #             break
        #         trans(now_amount - coin, now_amount)
        # return dp[amount]
# @lc code=end

