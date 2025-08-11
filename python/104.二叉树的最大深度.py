#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [root]
        layer = 0
        while queue:
            layer += 1
            t = queue
            queue = []
            for node in t:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return layer
# @lc code=end

