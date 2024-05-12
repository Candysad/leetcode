#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from collections import defaultdict
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            g[pre].append(course)
            indegree[course] += 1
        
        queue = []
        for i, d in enumerate(indegree):
            if d == 0:
                queue.append(i)
        
        while queue:
            t = queue
            queue = []
            for node in t:
                for nextnode in g[node]:
                    indegree[nextnode] -= 1
                    if indegree[nextnode] == 0:
                        queue.append(nextnode)
        return False if any(indegree) else True
# @lc code=end

