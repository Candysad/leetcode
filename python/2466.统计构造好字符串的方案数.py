#
# @lc app=leetcode.cn id=2466 lang=python3
#
# [2466] 统计构造好字符串的方案数
#
from functools import reduce
# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        '''
        爬楼梯问题
            一般问组合种类数量、能否到达
            内部组合数量，顺序影响种类
            连续相同选择不区分种类
        背包问题
            一般问最少选择次数（步数）、符合的组合种类数量
            顺序不影响种类
            重复顺序会导致遍历时间增加
        
        
        爬楼梯
        每次走 zero 步或 one 步
        问走上来一共多少种方法
        
        dp[i] 表示走到i的走法
        到达i只能是
            从 i-zero 走 zero 步上来
        或者从 i-one  走 one  步上来
        '''
        mod = 10 ** 9 + 7
        dp = [1] + [0] * high
        
        for i in range(min(zero, one), high+1):
            if i >= zero:
                dp[i] += dp[i-zero]
                dp[i] %= mod
            if i >= one:
                dp[i] +=  + dp[i-one]
                dp[i] %= mod

        return sum(dp[low:]) % mod
# @lc code=end

