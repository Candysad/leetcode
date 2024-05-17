#
# @lc app=leetcode.cn id=2685 lang=python3
#
# [2685] 统计完全连通分量的数量
#
from collections import defaultdict
# @lc code=start
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for node1, node2 in edges:
            g[node1].add(node2)
            g[node2].add(node1)
        for node in g:
            g[node].add(node)
        
        vis = set()
        result = 0
        
        def Component(node1):
            vis.add(node1)
            t = 1
            for node2 in g[node1]:
                vis.add(node2)
                if g[node1] != g[node2]:
                    t = 0
            return t
        
        for node in range(n):
            if node not in vis:
                result += Component(node)
        return result
'''
并查集
'''
# class Tree:
#     def __init__(self, n) -> None:
#         self.tree = [i for i in range(n)]
#         self.nodes = [set([i]) for i in range(n)]
    
#     def find(self, node):
#         while self.tree[node] != node:
#             node = self.tree[node]
#         return node
    
#     def merge(self, node1, node2):
#         head1, head2 = self.find(node1), self.find(node2)
#         if head1 > head2:
#             head1, head2 = head2, head1
        
#         self.tree[head2] = head1
#         self.nodes[head1].update(self.nodes[head2])
    
#     def count(self, grid):
#         vis = set()
#         result = 0
#         for i in range(len(self.tree)):
#             head = self.find(i)
#             if head not in vis:
#                 vis.add(head)
#                 t = 1
#                 for node in self.nodes[head]:
#                     if len(self.nodes[head].difference(set(grid[node]))) != 1:
#                         t = 0
#                         break
#                 if t:
#                     result += 1
#         return result

# class Solution:
#     def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
#         tree = Tree(n)
#         g = [[] for _ in range(n)]
        
#         for node1, node2 in edges:
#             tree.merge(node1, node2)
#             g[node1].append(node2)
#             g[node2].append(node1)
        
#         return tree.count(g)

# @lc code=end

