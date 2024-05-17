#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = (numBottles-numExchange) // (numExchange - 1) + 1
        return n+numBottles
# @lc code=end

