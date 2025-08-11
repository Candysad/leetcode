#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
from collections import defaultdict
# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tree = [i for i in range(n*n)]
        islands = defaultdict(list)
        signs = set()
        
        def find(node):
            while tree[node] != node:
                node = tree[node]
            return node
        
        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2: return
            if head1 > head2:
                head1, head2 = head2, head1
                node1, node2 = node2, node1
            tree[head2] = head1
            
        def optimize():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] and (i,j) in signs:
                        node = i*n + j
                        head = find(node)
                        islands[head].append((i, j))
        
        def search(i, j):
            sign = False
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y]:
                        merge(i*n + j, x*n + y)
                    else:
                        sign = True
            return sign
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    sign = search(i, j)
                    if sign:
                        signs.add((i, j))

        optimize()
        result = 2*n

        keys = list(islands.keys())
        for i, j in islands[keys[0]]:
            for x, y in islands[keys[1]]:
                dy = abs(y-j)
                dx = abs(x-i)
                result = min(result, dx + dy - 1)

        return result
# @lc code=end