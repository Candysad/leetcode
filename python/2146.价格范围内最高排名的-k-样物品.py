#
# @lc app=leetcode.cn id=2146 lang=python3
#
# [2146] 价格范围内最高排名的 K 样物品
#
# @lc code=start
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        low, high = pricing
        
        candidate = []
        if low <= grid[start[0]][start[1]] <= high:
            candidate.append((-1, grid[start[0]][start[1]], start[0], start[1]))
        
        layer = 0
        queue = [start]
        vis = set()
        vis.add(tuple(start))
        while queue:
            t = queue
            queue = []
            for i, j in t:
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in vis:
                        vis.add((x, y))
                        if low <= grid[x][y] <= high:
                           candidate.append((layer, grid[x][y], x, y))
                        
                        if grid[x][y] != 0:
                            queue.append((x, y))
            layer += 1
        candidate.sort()
        return [[x, y] for _, __, x, y in candidate[:k]]
# @lc code=end