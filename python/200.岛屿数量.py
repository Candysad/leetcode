#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from collections import deque
# @lc code=start
class uniontree:
    def __init__(self, grid, n, m):
        self.count = 0
        self.tree = [0] * m*n
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.tree[i*m + j] = i * m + j
                    self.count += 1
    
    def find(self, node):
        t = node
        while node != self.tree[node]:
            node = self.tree[node]
        self.tree[t] = node
        return node
    
    def merge(self, node1, node2):
        head1 = self.find(node1)
        head2 = self.find(node2)
        
        if head1 != head2:
            if head2 < head1:
                head1, head2 = head2, head1
            self.tree[head2] = head1
            self.count -= 1
        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        并查集
        并查集反而更慢了...
        '''
        n = len(grid)
        m = len(grid[0])
        tree = uniontree(grid, n, m)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = '0' # 不是广度优先，不需要先把相邻的置为 0
                                     # 一会相邻的还要再找相邻的，需要先保留 1
                    for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                        if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                            tree.merge(i*m+j, x*m+y)
        
        return tree.count
        
        '''
        广度优先搜索
        将能到达的1标记为-1
        '''
        # n = len(grid)
        # m = len(grid[0])
        # result = 0
        
        # def bfs(i, j):
        #     grid[i][j] = -1
        #     queue = [(i,j)]
        #     grid[i][j] = '0'
        #     while queue:
        #         t = queue
        #         queue = []
        #         for x, y in  t:
        #             for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        #                 if 0 <= xx < n and 0 <= yy < m and grid[xx][yy] == '1':
        #                     queue.append((xx, yy))
        #                     grid[xx][yy] = '0'
                        
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == '1':
        #             bfs(i,j)
        #             result += 1
        
        # return result
# @lc code=end

