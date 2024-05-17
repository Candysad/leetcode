#
# @lc app=leetcode.cn id=2642 lang=python3
#
# [2642] 设计可以求最短路径的图类
#
from heapq import *
from math import inf
# @lc code=start
class Graph:
    '''
    如果用广度优先每次添加都遍历一遍始终维护所有节点间的最短路径，时间复杂度太高了
    先存着，反正不会有重边
    要的时候再取，用优先队列优先遍历最近的，达到目标就结束，找完了找不到就是不通
    '''
    def __init__(self, n: int, edges: List[List[int]]):

        self.path = [[] for i in range(n)]
        for node1, node2, cost in edges:
            self.path[node1].append((cost, node2))

    def addEdge(self, edge: List[int]) -> None:
        self.path[edge[0]].append((edge[2], edge[1]))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [-1] * len(self.path)
        dist[node1] = 0
        queue = [(0, node1)] # 如果直接以node1的可到达点作为初始队列，会跳过第一次node1到他们的距离更新
        while queue:
            cost, mid_node  = heappop(queue)
            if mid_node == node2:
                return cost
            for end_cost, end_node in self.path[mid_node]:
                if dist[end_node] == -1 or dist[end_node] > end_cost + cost:
                    dist[end_node] = end_cost + cost
                    heappush(queue, (dist[end_node], end_node))
        return -1
    
    '''
    始终维护所有节点间的最短路径
    用优先队列都会超时...😓
    '''
    # def __init__(self, n: int, edges: List[List[int]]):
    #     self.n = n
    #     self.path = [[inf for i in range(n) ] for j in range(n)]
    #     for i in range(n):
    #         self.path[i][i] = 0
        
    #     for node1, node2, cost in edges:
    #         self.path[node1][node2] = cost
        
    #     for start in range(n):
    #         dis = [inf] * n
    #         queue = [(0, start)]
    #         vis = set()
    #         while queue:
    #             cost, mid = heappop(queue)
    #             if mid in vis:
    #                 continue
                
    #             vis.add(mid)
    #             for end in range(n):
    #                 if dis[end] > cost + self.path[mid][end]:
    #                     dis[end] = cost + self.path[mid][end]
    #                     heappush(queue, (dis[end], end))
                
    #             self.path[start] = dis
                        
    # def addEdge(self, edge: List[int]) -> None:
    #     node1, node2, cost = edge
    #     if cost < self.path[node1][node2]:
    #         self.path[node1][node2] = cost
    #         for start in range(self.n):
    #             dis = [inf] * self.n
    #             queue = [(0, start)]
    #             vis = set()
    #             while queue:
    #                 cost, mid = heappop(queue)
    #                 if mid in vis:
    #                     continue
                    
    #                 vis.add(mid)
    #                 for end in range(self.n):
    #                     if dis[end] > cost + self.path[mid][end]:
    #                         dis[end] = cost + self.path[mid][end]
    #                         heappush(queue, (dis[end], end))
                
    #             self.path[start] = dis

    # def shortestPath(self, node1: int, node2: int) -> int:
    #     return self.path[node1][node2] if self.path[node1][node2] != inf else -1
# @lc code=end