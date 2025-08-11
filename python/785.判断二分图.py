#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
# class Tree:
#     def __init__(self, n) -> None:
#         self.tree = [i for i in range(n)]
         
#     def find(self, node):
#         while node != self.tree[node]:
#             node = self.tree[node]
#         return node
            
#     def merge(self, node1, node2):
#         head1, head2 = self.find(node1), self.find(node2)
#         if head1 > head2:
#             head1, head2 = head2, head1
#         if self.tree[head2] != head1:
#             self.tree[head2] = head1
                           
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # n = len(graph)
        # tree = Tree(n)
        # for i in range(n):
        #     headi = tree.find(i)
        #     for j in range(1, len(graph[i])):
        #         if tree.find(graph[i][j]) == headi:
        #             return False
        #         tree.merge(graph[i][0], graph[i][j])

        # return True
        
        '''
        BFS 染色
        当前点应该是一个颜色，邻接点应该是另一个颜色
        如果一个点从一种颜色又被染成另一种颜色，说明集合交叉，不能二分
        '''
        n = len(graph)
        color = [0 for i in range(n)]
        
        def dfs(i, t):
            nonlocal result
            if color[i] != 0 and color[i] != t:
                result = False
                return
            
            color[i] = t
            for j in graph[i]:
                if color[j] == 0: # 只有color = 0的进入下一层
                    dfs(j, -t)
                elif color[j] != -t: # 已经染色的单独判断
                    result = False
                    return 

        result = True
        for i in range(n):
            if color[i] == 0:
                dfs(i, 1)
            if not result:
                break
        return result          
# @lc code=end

