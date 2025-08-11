#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i, p in enumerate(prices[:-1]):
            d = prices[i+1] - p
            if d > 0:
                result += d
        return result
        
# @lc code=end

