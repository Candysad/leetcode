#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
from itertools import pairwise
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        table = []
        
        def dfs(node):
            if node is None: return
            
            if node.left:
                dfs(node.left)
                
            table.append(node.val)
            
            if node.right:
                dfs(node.right)
        
        dfs(root)
        
        result = table[1] - table[0]
        for a, b in pairwise(table[1:]):
            result = min(b-a, result)
        return result
# @lc code=end