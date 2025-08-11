#
# @lc app=leetcode.cn id=851 lang=python3
#
# [851] 喧闹和富有
#

# @lc code=start
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        degree = [0] * n
        g = [[] for _ in range(n)]
        for a, b in richer:
            degree[b] += 1
            g[a].append(b)
        
        result = [i for i in range(n)]
        queue = []
        for i, d in enumerate(degree):
            if d == 0:
                queue.append(i)
        
        while queue:
            t = queue
            queue = []
            for node1 in t:
                for node2 in g[node1]:
                    degree[node2] -= 1
                    if quiet[result[node1]] < quiet[result[node2]]:
                        result[node2] = result[node1]
                    if degree[node2] == 0:
                        queue.append(node2)
        return result
# @lc code=end