#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        globalresult = 0
        def dfs(node):
            if node is None:
                return 2, inf, -inf, 0
            
            result = node.val
            tl, left_min, left_max, lresult = dfs(node.left)
            if tl == 2:
                left_min = node.val
            tr, right_min, right_max, rresult = dfs(node.right)
            if tr == 2:
                right_max = node.val
            
            if tl > 0 and tr > 0 and left_max < node.val < right_min:
                result += lresult + rresult
                nonlocal globalresult
                globalresult = max(result, globalresult)
                return 1, left_min, right_max, result
            else:
                result = max(lresult, rresult)
                return 0, -inf, inf, result
        
        dfs(root)
        return globalresult
# @lc code=end

