#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        queue = [poured]
        for i in range(1, query_row + 1):
            t = queue
            queue = [0] * (i + 1)
            for j in range(i + 1):
                if j < i:
                    queue[j] += max((t[j] - 1) / 2, 0)
                if j - 1 >= 0:
                    queue[j] += max((t[j - 1] - 1) / 2, 0)
        result = queue[query_glass]
        return  result if result < 1 else 1
# @lc code=end