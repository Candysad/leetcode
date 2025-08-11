#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from math import inf
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pre = inf
        result = 0
        for p in prices:
            result = max(p-min_pre, result)
            min_pre = min(p, min_pre)
        return result
# @lc code=end

