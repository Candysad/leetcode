#
# @lc app=leetcode.cn id=3122 lang=python3
#
# [3122] 使矩阵满足条件的最少操作次数
#
from functools import cache
from math import inf
from collections import Counter
# @lc code=start
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        counters = []
        for j in range(n):
            counter = Counter()
            for i in range(m):
                counter[grid[i][j]] += 1
            counters.append(counter)
        
        @cache
        def dfs(i, pre):
            if i == n: return 0
            # 换一个全都不是的
            t = m + dfs(i+1, -1)
            
            # 换一个现有的
            for num in counters[i]:
                if num  == pre: continue
                t = min(t, m-counters[i][num] + dfs(i+1, num))
            
            return t

        return dfs(0, -1)
# @lc code=end