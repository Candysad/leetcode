#
# @lc app=leetcode.cn id=1080 lang=python3
#
# [1080] 根到叶路径上的不足节点
#
from math import inf
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, pre):
            if node is None:
                return 0, False
            
            if not node.left and not node.right:
                left, cutleft = 0, False
                right, cutright = 0, False
            else:
                left, cutleft = -inf, False
                right, cutright = -inf, False
            
            if node.left is not None:
                left, cutleft = dfs(node.left, pre + node.val)
            if node.right is not None:
                right, cutright = dfs(node.right, pre + node.val)
            
            if cutleft:
                node.left = None
            if cutright:
                node.right = None
            
            _sum = max(left, right) + node.val
            return _sum, _sum < limit
        
        dfs(root, 0)
        print(root)
        return root
        
# @lc code=end

