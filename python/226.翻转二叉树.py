#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            
            t = node.left
            node.left = node.right
            node.right = t
            
        dfs(root)
        return root
        
# @lc code=end

