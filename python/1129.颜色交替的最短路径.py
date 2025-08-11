#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
#
from math import inf
# @lc code=start
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # g[0] 红色  g[1] 蓝色
        g = [[set() for _ in range(n)] for __ in range(2)]
        for a, b in redEdges:
            g[0][a].add(b)
        for a, b in blueEdges:
            g[1][a].add(b)
        
        dis = [0] + [inf] * (n-1)
        # vis[0] 从红色边到达node vis[1] 从蓝色到达
        vis = [set(), set()]
        
        # 0 红色来的 1 蓝色
        queue = [(0, 0), (0, 1)]
        layer = 0 # 当前广度优先搜索的层数（步数）
        while queue:
            t = queue
            queue = []
            for node1, color in t:
                nextcolor  = 0 if color == 1 else 1
                
                # 正常换颜色向后搜索
                for node2 in g[nextcolor][node1]:
                    if node2 not in vis[nextcolor]:
                        dis[node2] = min(dis[node2], layer + 1)
                        queue.append((node2, nextcolor))
                        vis[nextcolor].add(node2)
                
                # 存在另一种颜色的自环
                if node1 in g[nextcolor][node1] and node1 not in vis[color]:
                    queue.append((node1, nextcolor))
                    vis[color].add(node1)
            layer += 1

        return [d if d != inf else -1 for d in dis]
# @lc code=end