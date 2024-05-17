#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        pre = [0]
        result = []
        def dfs(i):
            if i == n-1:
                result.append(pre.copy())
                return
            
            for j in graph[i]:
                pre.append(j)
                dfs(j)
                pre.pop()
        dfs(0)
        return result 
# @lc code=end

