#
# @lc app=leetcode.cn id=2712 lang=python3
#
# [2712] 使所有字符相等的最小成本
#
from itertools import pairwise
from math import inf
# @lc code=start
class Solution:
    def minimumCost(self, s: str) -> int:
        '''
        合并动态规划
        每个相邻位置，不一样就要翻转一遍使两边变成一样
        左边确保相同，右边之前不一样的翻转后还是不一样
        '''
        n = len(s)
        if n == 1: return 0
        result = 0
        for i in range(1, n):
            if s[i-1] != s[i]:
                result += min(i, n-i)
        return result
        
        '''
        拆开遍历动态规划
        '''
        lasti = 0
        spans = []
        n = len(s)
        for i in range(n):
            if s[i] != s[lasti]:
                spans.append([int(s[lasti]), i-1, lasti])
                lasti = i
        spans.append([int(s[lasti]), n-1, lasti])
        
        n = len(spans)
        if n == 1:
            return 0
        dpleft  =  [[0, 0] for _ in range(n+1)] # 从左向右维护左半部
        dpright = [[0, 0] for _ in range(n+1)] # 右半部
        
        lastlefti  = -1
        lastrighti = len(s)
        for i in range(1, n+1):
            value, index = spans[i-1][0], spans[i-1][1]
            dpleft[i][value]   = dpleft[i-1][value]
            dpleft[i][1-value] = dpleft[i-1][value] + index + 1
            lastlefti = i

            i = n-i
            value, index = spans[i][0], spans[i][2]
            dpright[i][value]   = dpright[i+1][value]
            dpright[i][1-value] = dpright[i+1][value] + n - index + 1
            lastrighti = index
        result = inf
        for i, j in pairwise(range(n)):
            result = min(result, dpleft[i+1][0] + dpright[j][0], dpleft[i+1][1] +dpright[j][1])
        return result
# @lc code=end