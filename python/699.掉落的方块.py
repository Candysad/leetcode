#
# @lc app=leetcode.cn id=699 lang=python3
#
# [699] 掉落的方块
#
from collections import defaultdict
from bisect import bisect_left
# @lc code=start
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        result = [positions[0][1]]
        pres = [(positions[0][1], positions[0][0], positions[0][0] + positions[0][1])]
        nowmax = positions[0][1]
        n = len(positions)
        for i in range(1, n):
            nowhigh = positions[i][1]
            nl, nr = positions[i][0], positions[i][0] + positions[i][1]
            for j in range(i-1, -1, -1):
                phigh, pl, pr = pres[j]
                if (pl <= nl < pr) or (pl < nr <= pr) or (nl <= pl < pr <= nr):
                    nowhigh += phigh
                    break
            
            k = bisect_left(pres, nowhigh, key=lambda x: x[0])
            pres.insert(k, (nowhigh, nl, nr))
            
            nowmax = max(nowmax, nowhigh)
            result.append(nowmax)
        
        return result
# @lc code=end