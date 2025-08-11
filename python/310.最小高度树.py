#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        只找根节点，不用管具体在第几层
        叶子节点度总为1
        删去叶子节点之后会出现新的叶子节点
        删到只剩正中间或中间两个节点就是根了
        '''
        # if n == 1:
        #     return [0]
        
        # d = [0] * n # 记录所有节点的度
        # adjacent = [[] for _ in range(n)] # 记录所有节点的相邻节点，用来更新相邻节点的度
        
        # for u, v in edges:
        #     adjacent[u].append(v)
        #     adjacent[v].append(u)
        #     d[u] += 1
        #     d[v] += 1
        
        # remain = n
        # queue = [i for i, dd in enumerate(d) if dd == 1]
        
        # while remain > 2:
        #     t = queue
        #     queue = []
        #     remain -= len(t)
        #     for node in t:
        #         for ad in adjacent[node]:
        #             d[ad] -= 1
        #             if d[ad] == 1: # 新的叶子节点肯定和旧的相连
        #                 queue.append(ad)
            
        # return queue
    
        '''
        找最长路径
        最长路径中间的点（偶数两个奇数一个）就是答案
        技巧：找最长路径
            1.随便一个点找它的最远点
            2.从上一步得到的最远点出发找它的最远点
            3.两个最远点连起来就是最长路径
        遍历过程中留下节点间的顺序
        再回来根据留下的顺序信息得到完整的路径
        '''
        if n == 1:
            return [0]
        
        adjacent = [[] for _ in range(n)] # 记录所有节点的相邻节点，用来更新相邻节点的度
        for u, v in edges:
            adjacent[u].append(v)
            adjacent[v].append(u)
            
        parent = [0 for i in range(n)] # 记录每个遍历过的节点的上一层是哪个节点
        
        # 广度优先找最后一层即最远的点
        def bfs(start):
            visted = [0 for i in range(n)]
            visted[start] = 1
            queue = [start]
            now = start
            while queue:
                # print(queue)
                t = queue
                queue = []
                for node in t:
                    now = node
                    for ad in adjacent[node]:
                        if not visted[ad]:
                            visted[ad] = 1
                            queue.append(ad)
                            parent[ad] = node
                # print(now)
            return now
        
        # 最长路径 a → b
        a = bfs(0)
        # print('===')
        b = bfs(a)
        
        # print(a,b)
        # 用parent找路径完整过程
        # 因为找两头的时候是 a → b，所以记录的是前面作为后面的parent，找过程是从b开始找parent到a
        path = [b]
        now = parent[b]
        while now != a:
            path.append(now)
            now = parent[now]
        path.append(a)
        length = len(path)
        # print(path)
        return [path[length//2]] if length % 2 else  path[length//2-1: length//2+1]
# @lc code=end

