#
# @lc app=leetcode.cn id=2049 lang=python3
#
# [2049] 统计最高分的节点数目
#

# @lc code=start
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        degree = [0] * n
        for p in parents[1:]:
            degree[p] += 1

        queue = []
        for i, d in enumerate(degree):
            if d == 0:
                queue.append(i)
        
        table = [[1, 0, 0] for _ in range(n)]  
        while queue:
            t = queue
            queue = []
            for node in t:
                p = parents[node]

                if degree[p] == 2:
                    table[p][2] = table[node][0]
                else:
                    table[p][1] = table[node][0]
                table[p][0] += table[node][0]

                degree[p] -= 1
                if degree[p] == 0 and parents[p] != -1:
                    queue.append(p)
        
        def point(node):
            out = max(1, n-table[node][0])
            left = max(1, table[node][1])
            right = max(1, table[node][2])
            return out * left * right

        points = [point(node) for node in range(n)]
        return points.count(max(points))
# @lc code=end