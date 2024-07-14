#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
        
        result = [[inf] * n for _ in range(m)]
        vis = set(queue)
        layer = 0
        while queue:
            t = queue
            queue = []
            for i, j in t:
                result[i][j] = layer
                for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                    if 0 <= x < m and 0 <= y < n:
                        if (x, y) not in vis:
                            queue.append((x, y))
                            vis.add((x, y))
            layer += 1
        
        return result
# @lc code=end

