#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = [root]
        direct = 1
        
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
                result.append(layer[::direct])
            direct *= -1
        return result
# @lc code=end

