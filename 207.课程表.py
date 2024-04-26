#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from collections import defaultdict
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        d = [0] * numCourses # 入度
        for pre, suc in prerequisites:
            g[pre].append(suc)
            d[suc] += 1
        
        queue = []
        for node in range(numCourses): # 初始入度为 0 的节点
            if d[node] == 0:
                queue.append(node)
        
        while queue:
            t = queue
            queue = []
            for pre in t:
                for suc in g[pre]:
                    d[suc] -= 1
                    if d[suc] == 0:
                        queue.append(suc)
        
        return False if any(d) else True
# @lc code=end

