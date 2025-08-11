#
# @lc app=leetcode.cn id=2385 lang=python3
#
# [2385] 感染二叉树需要的总时间
#
from collections import defaultdict
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        '''
        递归建图得到边
        深度优先找最大深度   
        '''
        target = None
        g = defaultdict(list)
        def dfs(node):
            if node.val == start:
                nonlocal target
                target = node
                
            if node.left:
                g[node.val].append(node.left)
                g[node.left.val].append(node)
                dfs(node.left)
            if node.right:
                g[node.val].append(node.right)
                g[node.right.val].append(node)
                dfs(node.right)
            
        def spread(node, last):
            result = 0
            for s in g[node.val]:
                if s.val != last:
                    result = max(result, 1 + spread(s, node.val))
            return result

        dfs(root)
        return spread(target, 0)
# @lc code=end

