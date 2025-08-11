#
# @lc app=leetcode.cn id=2806 lang=python3
#
# [2806] 取整购买后的账户余额
#

# @lc code=start
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        t1 = purchaseAmount % 10
        t2 = purchaseAmount // 10
        result = (t2 + (1 if t1 >= 5 else 0) ) * 10
        return 100 - result
# @lc code=end