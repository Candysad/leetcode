#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        def dfs(iu, id, jl, jr):
            print(iu, id, jl, jr)
            if all(grid[i][j] == grid[iu][jl] for i in range(iu, id) for j in range(jl, jr)):
                return Node(grid[iu][jl] == 1, True)
            
            return Node(
                False,
                False,
                dfs(iu, (iu + id) // 2, jl, (jl + jr) // 2),
                dfs(iu, (iu + id) // 2, (jl + jr) // 2, jr),
                dfs((iu + id) // 2, id, jl, (jl + jr) // 2),
                dfs((iu + id) // 2, id, (jl + jr) // 2, jr)
            )
        
        return dfs(0, n, 0, n)
# @lc code=end