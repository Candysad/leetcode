#
# @lc app=leetcode.cn id=1765 lang=python3
#
# [1765] 地图中的最高点
#
from math import inf
# @lc code=start
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        queue = []
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = inf
        
        g = isWater
        layer = 1
        while queue:
            t = queue
            queue = []
            for i, j in t:
                for x, y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                    if 0 <= x < m and 0 <= y < n:
                        if g[x][y] > layer:
                            g[x][y] = layer
                            queue.append((x, y))
            
            layer += 1
        return g
# @lc code=end

