#
# @lc app=leetcode.cn id=2938 lang=python3
#
# [2938] 区分黑球与白球
#

# @lc code=start
class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        pre1 = 0
        for ball in s:
            if ball == '1':
                pre1 += 1
            else:
                result += pre1
        return result
# @lc code=end