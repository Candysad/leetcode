#
# @lc app=leetcode.cn id=2147 lang=python3
#
# [2147] 分隔长廊的方案数
#

# @lc code=start
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        c = corridor.count('S')
        if c == 0 or c % 2: return 0

        count = 0
        lasti = -1
        result = 1
        for i, c in enumerate(corridor):
            if c == 'S':
                count += 1
                if count == 2:
                    lasti = i
                if count == 3:
                    result *= i - lasti
                    count = 1
        return result % mod
# @lc code=end