#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        r = points[0][1]
        points.sort()
        result = 0
        for left, right in points:
            if left <= r:
                r = min(r, right)
            else:
                result += 1
                r = right
        
        return result + 1
# @lc code=end