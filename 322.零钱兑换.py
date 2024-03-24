#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        动态规划 背包题
        面值不一定符合常识，可能是完全不能凑成目标的几个数，也可能是刚好有特定组合可以凑出目标的一组
        coins [186,419,83,408]
        amount 6249
        还是只能动态规划
        
        题目amoun 最大 1000 数组最长1000，但是实际问题中会不会太大了？
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
        
        '''
        位运算技巧
        这还算动态规划吗？
        '''
        dp = 1 << amount 
        result = 0
        while dp & 1 == 0:
            t = dp
            for coin in coins:
                dp |= t >> coin
            if dp == t:
                return -1
            result += 1
        return result
        
# @lc code=end

