#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] 概率最大的路径
#
from heapq import *
# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            w = succProb[i]
            g[a].append([b, w])
            g[b].append([a, w])
        
        if len(g[start_node]) == 0 or len(g[end_node]) == 0:
            return 0
        
        dis = [0] * n
        dis[start_node] = 1
        queue = [(-1, start_node)]
        while queue:
            w, node = heappop(queue)
            w = -w
            if w < dis[node]:
                continue
              
            for nextnode, ww in g[node]: 
                new = w * ww
                if dis[nextnode] < new:
                    dis[nextnode] = new
                    heappush(queue, (-new, nextnode))
        
        return dis[end_node]
# @lc code=end

