#
# @lc app=leetcode.cn id=2320 lang=python3
#
# [2320] 统计放置房子的方式数
#

# @lc code=start
class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dpu, dpd, dpud, dpn = 0, 0, 0, 1,
        for i in range(n):
            u = dpn + dpd
            d = dpn + dpu
            ud = dpn
            dpn = (dpu + dpd + dpud + dpn) % mod
            
            dpu, dpd, dpud = u % mod, d % mod, ud % mod
        return (dpu + dpd + dpud + dpn) % mod
# @lc code=end