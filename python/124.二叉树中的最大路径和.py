#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return -inf, -inf
            
            left, downl = dfs(node.left)
            right, downr = dfs(node.right)
            # 向上走
            # 经过当前点，上一层可以连在这里
            # 左，右，只有自己
            up = max(node.val + left, node.val + right, node.val)
            # 从下面走，下面来的连不上，但是可能单独成为路径
            down = max(downl, downr, left + right + node.val, left, right)

            return up, down
            
        return max(dfs(root))
        
# @lc code=end

