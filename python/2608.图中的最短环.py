#
# @lc app=leetcode.cn id=2608 lang=python3
#
# [2608] 图中的最短环
#
from math import inf
# @lc code=start
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def find(start):
            result = inf
            dis = [inf] * n
            dis[start] = 0
            queue = [(start, -1)]
            while queue:
                t = queue
                queue = []
                for node, pre in t:
                    for nextnode in g[node]:
                        if dis[nextnode] == inf:
                            dis[nextnode] = dis[node] + 1
                            queue.append((nextnode, node))
                        elif nextnode != pre:
                            result = min(result, dis[node] + dis[nextnode] + 1)
            
            return result

        result = min((find(node) for node in range(n)))
        return result if result != inf else -1
# @lc code=end