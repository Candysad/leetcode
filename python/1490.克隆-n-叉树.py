#
# @lc app=leetcode.cn id=1490 lang=python3
#
# [1490] 克隆 N 叉树
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None: return None
        result = Node(root.val)
        
        queue = [(root, result)]
        while queue:
            t = queue
            queue = []
            for node, now in t:
                for c in node.children:
                    t = Node(c.val)
                    now.children.append(t)
                    queue.append((c, t))
        
        return result
        
            
        
        
# @lc code=end