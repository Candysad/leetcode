#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
from math import inf
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        空间改进
        '''
        n = len(prices)
        if n == 1:
            return 0
        
        # 每2个一组，第1个为有股票，第2个为没股票
        dp = [-inf]*k*2
        for j in range(k):
            dp[j*2+1] = 0  # 初始没交易过的收益就是0，配合 -inf 确保有收益一定更新
        dp[0] = -prices[0] # 第一次第一天买入
        
        for i in range(1, n):
            # 第一次交易没有再上一次交易可以回溯
            # 第一次交易过程中，有股票则一定是空手花钱买了一次，要么今天买，要么以前就买了
            dp[0] = max(-prices[i], dp[0])
            # d1 记录这一轮卖出去的收益
            dp[1] = max(dp[0] + prices[i], dp[1]) # 今天卖或者之前已经卖了
            for j in range(1, k):
                # 在后续的第j次交易中，有股票则是本轮之前已经买了，或者今天刚买(上一轮结束的收益+今天的支出)
                dp[j*2] = max(dp[j*2], dp[(j-1)*2+1]-prices[i])
                # 没有股票则是今天已经卖出去了，或者之前卖出去了
                dp[j*2+1] = max(dp[j*2]+prices[i], dp[j*2+1])

        return max(dp)
        
        
        '''
        只限制购买次数，没有额外条件
        使dp[i]里面包含0...k-1次交易中的信息
        dp[i][j] 为已完成j次，当前进行第j+1次交易
        
        dp[i] =  截止当天不同状态下的最大收益
            第j次交易中今天有股票（已购买第j次）
            第j次交易中今天没股票（已完成第j次交易）
        '''
        # n = len(prices)
        # if n == 1:
        #     return 0
        
        # # 每2个一组，第1个为有股票，第2个为没股票
        # dp = [[-inf]*k*2 for _ in range(n)]
        # for j in range(k):
        #     dp[0][j*2+1] = 0  # 初始没交易过的收益就是0，配合 -inf 确保有收益一定更新
        # dp[0][0] = -prices[0] # 第一次第一天买入
        
        # for i in range(1, n):
        #     # 第一次交易没有再上一次交易可以回溯
        #     # 第一次交易过程中，有股票则一定是空手花钱买了一次，要么今天买，要么以前就买了
        #     dp[i][0] = max(-prices[i], dp[i-1][0])
        #     # d1 记录这一轮卖出去的收益
        #     dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1]) # 今天卖或者之前已经卖了
        #     for j in range(1, k):
        #         # 在后续的第j次交易中，有股票则是本轮之前已经买了，或者今天刚买(上一轮结束的收益+今天的支出)
        #         dp[i][j*2] = max(dp[i-1][j*2], dp[i-1][(j-1)*2+1]-prices[i])
        #         # 没有股票则是今天已经卖出去了，或者之前卖出去了
        #         dp[i][j*2+1] = max(dp[i-1][j*2]+prices[i], dp[i-1][j*2+1])

        # return max(dp[-1])
# @lc code=end

