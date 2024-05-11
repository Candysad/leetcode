#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
from collections import defaultdict
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        g = defaultdict(set)
        n = 0
        def dfs(node):
            if node is None:
                return
            nonlocal n
            n = max(n, node.val)
            for neighbor in node.neighbors:   
                g[neighbor.val].add(node.val)
                if neighbor.val not in g[node.val]:
                    g[node.val].add(neighbor.val)
                    dfs(neighbor)
        dfs(node)
        if n == 0:
            return None
        elif n == 1:
            return Node(1, None)

        nodes = [0] + [Node(val=i) for i in range(1,n+1)]
        for i in range(1, n+1):
            for neighbor in g[i]:
                nodes[i].neighbors.append(nodes[neighbor])
        return nodes[1]
        
# @lc code=end

