#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        
        queue = [(root, 0)]
        while queue:
            t = queue
            queue = []
            
            for node, pre in t:
                pre += node.val
                if node.left is None and node.right is None:
                    if pre == targetSum: return True
                
                if node.left is not None:
                    queue.append((node.left, pre))
                if node.right is not None:
                    queue.append((node.right, pre))
        
        return False
# @lc code=end