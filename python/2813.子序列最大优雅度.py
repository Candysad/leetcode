#
# @lc app=leetcode.cn id=2813 lang=python3
#
# [2813] 子序列最大优雅度
#
from math import inf
from heapq import *
from collections import defaultdict
# @lc code=start
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        if k == 1: return max(items, key=lambda x: x[0])[0] + 1
        
        _sum = 0
        cn = set()
        morethanone = []
        items.sort(key=lambda x: -x[0])

        for num, cate in items[:k]:
            _sum += num
            if cate not in cn:
                cn.add(cate)
            else:
                morethanone.append(num)
        
        result = _sum + len(cn)**2
        for num, cate in items[k:]:
            if cate in cn: continue
            if morethanone:
                cn.add(cate)
                _sum = _sum - morethanone.pop() + num
                result = max(_sum + len(cn)**2, result)
       
        return result

# @lc code=end