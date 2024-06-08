#
# @lc app=leetcode.cn id=1377 lang=python3
#
# [1377] T 秒后青蛙的位置
#
from collections import defaultdict
# @lc code=start
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if target == 1: return 0
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        path = []
        def dfs(t, now, pre):
            if now == target:
                if t != 0 and g[now] != 1:
                    return 0
                else:
                    return 1
            if t == 0:
                return -1
            
            result = None
            for next in g[now]:
                if next != pre:
                    path.append(next)
                    result = dfs(t-1, next, now)
                    if result == -1:
                        path.pop()
                    else:
                        return result
            return -1
            
        path.append(1)
        result = dfs(t, 1, -1)
        if result == 0: return 0
        
        print(g)
        print(path)
        result = 1 / len(g[1])
        for node in path[1:-1]:
            print(len(g[node])-1)
            result *= 1 / (len(g[node]) - 1)
        return result
         
# @lc code=end