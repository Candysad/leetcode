#
# @lc app=leetcode.cn id=2642 lang=python3
#
# [2642] 设计可以求最短路径的图类
#
from math import inf
from heapq import *
from collections import defaultdict
# @lc code=start
class Graph:
    '''
    存路径
    查的时候现场 Dijkstra
    '''
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = defaultdict(list)
        for a, b, w in edges:
            self.g[a].append([b, w])
        

    def addEdge(self, edge: List[int]) -> None:
        a, b, w = edge
        self.g[a].append([b, w])


    def shortestPath(self, node1: int, node2: int) -> int:
        dis = [inf] * self.n
        dis[node1] = 0
        queue = [[0, node1]]
        while queue:
            w, b = heappop(queue)
            if dis[b] < w: continue
            if b == node2:
                return w
            
            for c, ww in self.g[b]:
                cost = w + ww
                if cost < dis[c]:
                    dis[c] = cost
                    heappush(queue, [c, cost])
        return -1 if dis[node2] == inf else dis[node2]
# @lc code=end