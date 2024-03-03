#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 异或留下不同的位置，然后数
        x ^= y
        count = 0
        while x :
            count += 1
            x &= x - 1
        return count
# @lc code=end

