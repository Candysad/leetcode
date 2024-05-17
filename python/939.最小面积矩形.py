#
# @lc app=leetcode.cn id=939 lang=python3
#
# [939] 最小面积矩形
#
from math import inf
from collections import defaultdict
# @lc code=start
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ps = set([(p[0], p[1]) for p in points])
        points.sort()
        n = len(points)
        result = inf
        for i in range(n-1):
            tl = points[i]
            for j in range(i+1, n):
                br = points[j]

                if br[0] > tl[0] and br [1] > tl[1]:
                    if (tl[0], br[1]) in ps and (br[0], tl[1]) in ps:
                        result = min(result, (br[0] - tl[0]) * (br[1] - tl[1]))
        
        return 0 if result == inf else result
# @lc code=end

