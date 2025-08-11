#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, _max, _min):
            if node == None:
                return -1
            
            t = max(abs(node.val - _max), abs(node.val - _min))
            _max = max(_max, node.val)
            _min = min(_min, node.val)
            
            left = dfs(node.left, _max, _min)
            right = dfs(node.right, _max, _min)
            
            return max(t, left, right)

        return dfs(root, root.val, root.val)
# @lc code=end

