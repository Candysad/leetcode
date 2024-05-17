#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        queue = [root]
        while queue:
            t = queue
            queue = []
            layer = []
            for node in t:
                if node is not None:
                    layer.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if layer:
                result.append(layer)
        
        return result[::-1]
# @lc code=end

