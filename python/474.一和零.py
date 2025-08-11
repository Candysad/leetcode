#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        table = []
        for s in strs:
            _1 = s.count('1')
            _0 = len(s) - _1
            table.append((_0, _1))
        
        nt = len(table)
        @cache
        def dfs(i, ms, ns):
            if i == nt: return 0

            t = dfs(i+1, ms, ns)
            if ms >= table[i][0] and ns >= table[i][1]:
                t = max(t, dfs(i+1, ms-table[i][0], ns-table[i][1]) + 1)
            return t
        
        return dfs(0, m, n)
# @lc code=end