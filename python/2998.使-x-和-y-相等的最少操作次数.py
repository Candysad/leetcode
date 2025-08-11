#
# @lc app=leetcode.cn id=2998 lang=python3
#
# [2998] 使 X 和 Y 相等的最少操作次数
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y-x
        '''
        DFS
        '''
        @cache
        def dfs(x):
            if x < y:
                return  y-x
            if x == y:
                return 0
            
            t = inf
            # 变成11或5的倍数，往下变或往上变
            t = min(t, dfs(x // 11) + x % 11 + 1)
            t = min(t, dfs(x//11 + 1) + 11-x%11 + 1)
            t = min(t, dfs(x // 5) + x % 5 + 1)
            t = min(t, dfs(x//5 + 1) + 5-x%5 + 1)
            t = min(x-y) # 比y大，直接减取差距便过去
            return t
            
        return dfs(x)
        
        '''
        BFS
        '''
        # if x <= y:
        #     return y-x
        # vis = set()
        # queue = [x]
        # layer = 0
        # while queue:
        #     t = queue
        #     queue = []
        #     for x in t:
        #         if x == y:
        #             return layer

        #         if x % 11 == 0 and x // 11 not in vis:
        #             vis.add(x//11)
        #             queue.append(x//11)
        #         if x % 5 == 0 and x // 5 not in vis:
        #             vis.add(x//5)
        #             queue.append(x//5)
        #         if x + 1 not in vis:
        #             vis.add(x+1)
        #             queue.append(x+1)
        #         if x - 1 not in vis:
        #             vis.add(x-1)
        #             queue.append(x-1)
        #     layer += 1
# @lc code=end

