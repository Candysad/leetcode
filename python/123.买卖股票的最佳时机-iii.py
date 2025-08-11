#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        完成两笔交易
        那就用 dp 存每天完成了一笔交易的最大收益
        然后遍历过程中完成第二笔，记录第二笔之后最大收益
        
        dp[i] = (
            今天手里有股票（第一次）的收益
                今天买的，之前没买过股票
                之前就买了，昨天有股票
            今天手里没股票（第一次已经卖了）的收益
                今天卖的，昨天结束时有股票
                之前就卖了，昨天就没股票
            今天手里没股票（还没买过）的收益，固定是0
                之前也没买过
        )
        
        第二次交易最早在第三天开始买，最晚在倒数第二天买
        第二次交易后的收益是之前第一次交易后的收益+第二次的收益
        dp = (
            今天手里有股票（第二次）的收益
                今天买的，之前已经 完成第一次交易 所以没有股票
                今天买的，今天刚第一次卖就马上买
                之前就买了（第二次买）
            今天手里没有，第二次交易已经完成
                今天卖了（昨天结束时有第二次买的股票），得到收益，更新最大值
                之前就卖了，不记录
            今天手里没有，之前也没买第二次，不尝试第二次交易
                仍然是第一次交易结束后的收益
        )
        
        同一天可以又买又卖.....
        '''
        n = len(prices)
        if n == 1:
            return 0
        
        dp = [[-prices[0], 0]]
        
        # 只交易一次的收益
        for i in range(1, n):
            d0 = max(-prices[i], dp[i-1][0])
            d1 = max(dp[-1][0] + prices[i], dp[-1][1])
            # d2 = 0
            dp.append([d0, d1])
        
        if n == 2:
            return dp[1][1]
        
        # 第二次交易
        dp[2][0] = dp[1][1] - prices[2] # 第二笔交易第一次在第3天买
        result = dp[2][1]
        
        for i in range(3, n):
            d0 = max(dp[i-1][1]-prices[i], dp[i][1]-prices[i], dp[i-1][0])
            d1 = max(dp[i-1][0] + prices[i], dp[i][1])
            dp[i][0] = d0
            result = max(result, d1)
        return result
        
# @lc code=end

