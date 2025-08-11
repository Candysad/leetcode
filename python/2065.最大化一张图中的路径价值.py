#
# @lc app=leetcode.cn id=2065 lang=python3
#
# [2065] 最大化一张图中的路径价值
#
from collections import defaultdict
# @lc code=start
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        g = defaultdict(list)
        
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))
        
        vis = set()
        result = 0
        def dfs(node, prev, restime):
            if node == 0:
                nonlocal result
                result = max(prev, result)
            
            for nextnode, w in g[node]:
                if restime >= w:
                    if nextnode in vis:
                        dfs(nextnode, prev, restime-w)
                    else:
                        vis.add(nextnode)
                        dfs(nextnode, prev + values[nextnode], restime-w)
                        vis.remove(nextnode)
        
        vis.add(0)
        dfs(0, values[0], maxTime)
        return result
# @lc code=end