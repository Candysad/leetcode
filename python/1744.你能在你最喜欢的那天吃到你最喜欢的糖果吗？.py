#
# @lc app=leetcode.cn id=1744 lang=python3
#
# [1744] 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
#
from itertools import accumulate
# @lc code=start
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pres = list(accumulate(candiesCount))
        
        result = []
        for ci, day, cap in queries:
            candymax = pres[ci]
            candymin = 1 + (pres[ci-1] if ci else 0)
            
            eatmax = cap * (day + 1) 
            eatmin = day + 1
            
            # 判断两个区间有无重叠
            # 一前一后
            t = eatmin <= candymin <= eatmax
            t |= candymin <= eatmin <= candymax
            
            # 一个包住另一个
            t |= eatmin <= candymin and candymax <= eatmax
            t |= candymin <= eatmin and eatmax <= candymax
            result.append(t)
        return result
# @lc code=end