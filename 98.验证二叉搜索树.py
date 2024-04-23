#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, _min, _max):
            if node is None:
                return True
            
            if _min < node.val < _max:
                return dfs(node.left, _min, node.val) & dfs(node.right, node.val, _max)
            
            return False
                
        return dfs(root, -inf, inf)
        
# @lc code=end

