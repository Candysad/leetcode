#
# @lc app=leetcode.cn id=1976 lang=python3
#
# [1976] 到达目的地的方案数
#

# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        '''
        优先队列 Dijkstra 找路径
        动态规划记录路径数目
        
        inf leetcode引入了math包，里面带了inf
        '''
        # 题目要求取余
        mod = 10**9 + 7
        
        # 路径
        edge = [[inf] * n for _ in range(n)]
        for u, v, t in roads:
            edge[u][v] = edge[v][u] = t
        
        # 起点到其余点的距离
        # 优先队列找
        dis = [0] + [inf] * (n-1)
        
        # 动态规划找
        # 从起点到点i的最小路径的数目
        count_ways = [1] + [0] * (n-1)
        
        # 优先队列维护当前可到达点及其距离
        # 从起点开始
        # 优先路径是小根堆，每次找到新的当前最短路径时
        # 插入起点到新路径节点的最短距离
        # 之前插入的距离会留在堆底，弹出时不如先弹出的小，不会被更新
        pq = [(0, 0)]
        while pq:
            t, u = heappop(pq) # 当前可以到达的节点中距离起点最近的
            if t > dis[u]: # 记录的距离比当前还长 
                continue   # 说明时旧的最短距离
                           # 不需要
            # 从当前最近节点出发 更新最短距离
            for v in range(n):
                w = edge[u][v]
                if t + w < dis[v]:
                    dis[v] = t + w
                    count_ways[v] = count_ways[u] # 有更新最短距离时
                                                  # 到达该点的最短路径个数
                                                  # 等于从上个点来的最短路径数目
                    heappush(pq, (t + w, v)) # 更新一轮当前到达各个节点的最短距离
                
                elif t + w == dis[v]: 
                    count_ways[v] = (count_ways[u] + count_ways[v]) % mod
                    # 有相同最短路径时
                    # 到该点的最短路径可以不从上个点来
                    # 总最短路径个数为两者之和
                    # Dijkstra 同时保证了不会重复数，每次只遍历当前最近的
                    
        return count_ways[-1]     
# @lc code=end

