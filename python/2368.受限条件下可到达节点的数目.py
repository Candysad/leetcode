#
# @lc app=leetcode.cn id=2368 lang=python3
#
# [2368] 受限条件下可到达节点的数目
#

# @lc code=start

def find(woods:List, node:int):
    while woods[node] != node:
        node = woods[node]
    return node

def merge(woods:List, node1:int, node2:int):
    root1 = find(woods, node1)
    root2 = find(woods, node2)
    if root1 < root2:
        woods[root2] = root1
    else:
        woods[root1] = root2

def optim(woods:List, n):
    for i in range(n):
        woods[i] = find(woods, i)

class Solution:
    def __init__(self) -> None:
        self.count = 1
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        '''
        DFS
        
        map = [[] * n for _ in range(n)]
        for e in edges:
            if e[0] not in restricted and e[1] not in restricted:
                map[e[0]].append(e[1])
                map[e[1]].append(e[0])
        # print(map)
        
        def dfs(now:int, pre:int):
            # print(now, pre)
            for node in map[now]:
                if node != pre:
                    self.count += 1
                    dfs(node, now)
                    
        dfs(0, -1)
        return self.count
        '''
        # is_restricted = [0] * n
        # for x in restricted:
        #     is_restricted[x] = 1
        # g = [[] for _ in range(n)]
        # for v in edges:
        #     g[v[0]].append(v[1])
        #     g[v[1]].append(v[0])

        # cnt = 0
        # def dfs(x, f):
        #     nonlocal cnt
        #     cnt += 1
        #     for y in g[x]:
        #         if y != f and not is_restricted[y]:
        #             dfs(y, x)

        # dfs(0, -1)
        # return cnt
        
        '''
        并查集
        受限节点不用出入，其相关的边都不会用，直接跳过
        用剩下的边构建并查集
        需要数数所以最后整体优化一次并查集
        '''
        woods = [i for i in range(n)]
        access = [1] * n
        for r in restricted:
            access[r] = 0
            
        for e in edges:
            if access[e[0]] and access[e[1]]:
                merge(woods, e[0], e[1])
        optim(woods, n)
        
        result = 0
        root0 = woods[0]
        for node in woods:
            if node == root0:
                result += 1
        return result  
# @lc code=end

