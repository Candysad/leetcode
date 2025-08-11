#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        单次买或卖不算交易
        你完成一次（买+卖）才算，也就是手续费只在你完成卖的时候扣除
        '''
        n = len(prices)
        if n == 0:
            return 0

        d0 = -prices[0]       # 手里有
                              #     可能是之前就有，可能是今天刚买
                              #     不会是今天卖了又买，卖了能赚则之前买的一定更便宜
                              #     今天又买又卖的进出交易额相同，反而还要吃手续费，后续成本也变高了 
        d1 = 0                # 手里没有
                              #     今天刚卖，或者之前就卖了
        for i in range(1, n):
            d0 = max(d0, d1 - prices[i])
            d1 = max(d1, d0 + prices[i] - fee)
        
        return max(d0, d1)
    
        
# @lc code=end

