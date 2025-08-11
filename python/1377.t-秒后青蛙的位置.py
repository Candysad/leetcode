#
# @lc app=leetcode.cn id=1377 lang=python3
#
# [1377] T 秒后青蛙的位置
#
from collections import defaultdict
# @lc code=start
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # 目标就是 1，除非全图只有1，否则就是 0 概率
        if target == 1:
            if len(edges) == 0:
                return 1
            else:
                return 0

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        path = [] # 记录来的路
        def dfs(t, now, pre):
            if now == target:
                # 找到了但是时间没耗尽且还能走到其他地方
                if t != 0 and len(g[now]) != 1:
                    return 0
                else: # 找到了耗尽了或者找到了只能原地踏步
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
        # 找到了，但是没停下来
        if result == 0: return 0
        # 来不及，找不到
        if path[-1] != target: return 0
        # 来得及，找得到，能停下来
        result = 1 / len(g[1])
        for node in path[1:-1]: # path 最后一个是自己，算概率的时候不用
            result *= 1 / (len(g[node]) - 1)
        return result
# @lc code=end