#
# @lc app=leetcode.cn id=2368 lang=python3
#
# [2368] 受限条件下可到达节点的数目
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.count = 1
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        '''
        DFS
        '''
        # map = [[] * n for _ in range(n)]
        # for e in edges:
        #     if e[0] not in restricted and e[1] not in restricted:
        #         map[e[0]].append(e[1])
        #         map[e[1]].append(e[0])
        # # print(map)
        
        # def dfs(now:int, pre:int):
        #     # print(now, pre)
        #     for node in map[now]:
        #         if node != pre:
        #             self.count += 1
        #             dfs(node, now)
                    
        # dfs(0, -1)
        # return self.count

        is_restricted = [0] * n
        for x in restricted:
            is_restricted[x] = 1
        g = [[] for _ in range(n)]
        for v in edges:
            g[v[0]].append(v[1])
            g[v[1]].append(v[0])

        cnt = 0
        def dfs(x, f):
            nonlocal cnt
            cnt += 1
            for y in g[x]:
                if y != f and not is_restricted[y]:
                    dfs(y, x)

        dfs(0, -1)
        return cnt
# @lc code=end

