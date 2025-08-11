#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
from collections import deque
from math import inf
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        广度优先搜索
        每个烂橘子都光度搜索一次，更新自己周围所有新鲜橘子的最少烂掉的时间
        每个新鲜橘子都判断一下四周有没有烂的，如果没有说明不会烂
        返回新鲜橘子的最大烂掉的时间
        
        0 空
        1 新鲜
        2 一开始就是烂的
        -x 新鲜橘子烂掉的最少时间
        '''
        n = len(grid)
        m = len(grid[0])
        
        def bfs(i, j):
            vis = set()
            queue = [(i, j)]
            time = 0
            while queue:
                t = queue
                queue = []
                time += 1
                for x, y in t:
                    if (x, y) not in vis:
                        vis.add((x,y))
                        for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                            if 0 <= xx < n and 0 <= yy < m:
                                if grid[xx][yy] != 0 and grid[xx][yy] != 2:
                                    grid[xx][yy] = -time if grid[xx][yy] == 1 else max(grid[xx][yy], -time)
                                    queue.append((xx,yy))
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    bfs(i, j)
    
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: # 还有新鲜的
                    return -1
                if grid[i][j] < 0:
                    result = min(result, grid[i][j])
        return -result

# @lc code=end