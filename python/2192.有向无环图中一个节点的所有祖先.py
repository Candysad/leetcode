#
# @lc app=leetcode.cn id=2192 lang=python3
#
# [2192] 有向无环图中一个节点的所有祖先
#
# @lc code=start
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:     
        '''
        拓扑排序
        '''
        g = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            g[a].append(b)
            degree[b] += 1
        
        result = [set() for _ in range(n)]
        queue = [i for i in range(n) if degree[i] == 0]
        
        while queue:
            t = queue
            queue = []
            for a in t:
                for b in g[a]:
                    result[b].add(a)
                    result[b].update(result[a])
                    degree[b] -= 1
                    if degree[b] == 0:
                        queue.append(b)
        
        for i in range(n):
            result[i] = sorted(list(result[i]))
        return result
# @lc code=end

