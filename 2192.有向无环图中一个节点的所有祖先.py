#
# @lc app=leetcode.cn id=2192 lang=python3
#
# [2192] 有向无环图中一个节点的所有祖先
#
# @lc code=start
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''
        有向无环图
        拓扑排序
        每次遍历入度为0的节点，保证更早的节点总是先被遍历
        '''
        ancestors = [set() for _ in range(n)]
        adjacent = [[] for _ in range(n)]
        degree = [0] * n
        for _from, _to in edges:
            degree[_to] += 1
            adjacent[_from].append(_to)
        
        queue = []
        for node, d in enumerate(degree):
            if d == 0:
                queue.append(node)
        
        while queue:
            t = queue
            queue = []
            for parent in t:
                for child in adjacent[parent]:
                    ancestors[child].add(parent)
                    ancestors[child].update(ancestors[parent])
                    
                    degree[child] -= 1
                    if degree[child] == 0:
                        queue.append(child)
        return [sorted(ancestors[i]) for i in range(n)]
         
        '''
        Counter 存
        遍历两轮一定能全塞进去，但是会超时
        '''
        # parent = [[] for _ in range(n)]
        # for fro, to in edges:
        #     parent[to].append(fro)
        
        # ancestors = [Counter(p) for p in parent]
        # def dfs(now, anc):
        #     ancs = list(ancestors[anc].keys()).copy()
        #     ancestors[now] += ancestors[anc]
        #     for ances in ancs:
        #         dfs(now, ances)
            
        # for now in range(n):
        #     dfs(now, now)
        
        # for now in range(n):
        #     dfs(now, now)
        
        # result = [list(now.keys()) for now in ancestors]
        # for now in result:
        #     now.sort()
        # return result
# @lc code=end

