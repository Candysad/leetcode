#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        result = 0
        queue = [root]
        while queue:
            t = queue
            queue = []
            result += len(t)
            for node in t:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
# @lc code=end