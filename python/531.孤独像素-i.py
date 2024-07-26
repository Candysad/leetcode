#
# @lc app=leetcode.cn id=531 lang=python3
#
# [531] 孤独像素 I
#
from collections import defaultdict
from functools import reduce
# @lc code=start
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        
        result = defaultdict(int)
        candidate = set()
        for i in range(m):
            if picture[i].count('B') == 1:
                candidate.add(picture[i].index('B'))
            for j in range(n):
                if picture[i][j] == 'B':
                    result[j] += 1
        
        return sum(1 if result[key] == 1 else 0 for key in candidate)
# @lc code=end