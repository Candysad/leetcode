#
# @lc app=leetcode.cn id=2360 lang=python3
#
# [2360] 图中的最长环
#

# @lc code=start
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        degree = [0] * n
        
        for b in edges:
            degree[b] = 1
        
        queue = []
        for i in range(n):
            if edges[i] != -1 and degree[i]:
                queue.append(i)
        
        vis = set()
        def check(node):
            layer = 0
            path = {}
            while node not in path:
                path[node] = layer
                layer += 1
                
                if node in vis:return -1
                if edges[node] == -1: return -1
                node = edges[node]
            vis.update(path.keys())
            return layer - path[node]
        
        result = -1
        for node in queue:
            result = max(result, check(node))
        
        return result
# @lc code=end