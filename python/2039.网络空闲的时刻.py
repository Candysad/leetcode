#
# @lc app=leetcode.cn id=2039 lang=python3
#
# [2039] 网络空闲的时刻
#
from collections import defaultdict
from heapq import *
from math import inf
# @lc code=start
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        g = defaultdict(list)
        n = 0
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            n = max(n, a, b)
            
        queue = [0]
        layer = 0
        vis = set()
        result = 0
        while queue:
            t = queue
            queue = []
            for node in t:
                d = 2*layer
                p = patience[node]
                ps = d// p
                pt = (ps-1) * p + d
                result = max(pt, result)

                for nextnode in g[node]:
                    if nextnode not in vis:
                        queue.append(nextnode)
                        vis.add(nextnode)
        return result + 1
        
        '''
        Dijkstra
        '''
        g = defaultdict(list)
        n = 0
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            n = max(n, a, b)
            
        queue = [(0, 0)]
        dis = [0] + [inf] * n
        while queue:
            d, a = heappop(queue)
            
            if d > dis[a]: continue
            
            for b in g[a]:
                if d + 1 < dis[b]:
                    dis[b] = d + 1
                    heappush(queue, (d+1, b))
        
        result = 0
        for i in range(1, n+1):
            p = patience[i]
            
            # 来回距离，第一个包返回来的时间
            d = 2 * dis[i]
            
            # 等待时间发包次数，即等待了几个 p
            # 减 1 避免恰好最后一次收到又发了
            ps = (d-1) // p 
            # 等待总时间，最后一次发包时间
            pt = ps * p
            # 最后一次收包时间
            t = pt + d
            
            result = max(result, t)
        return result   
# @lc code=end