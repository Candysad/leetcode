#
# @lc app=leetcode.cn id=333 lang=python3
#
# [333] 最大二叉搜索子树
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
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            if node is None:
                return 1, inf, -inf, 0
            
            leftt, leftmin, leftmax, leftc = dfs(node.left)
            rightt, rightmin, rightmax, rightc = dfs(node.right)

            if leftt and rightt:
                if leftmax < node.val < rightmin:
                    nonlocal result
                    c = leftc + rightc + 1
                    result = max(result, c)
                    return 1, leftmin if leftmin != inf else node.val, rightmax if rightmax != -inf else node.val, c
            
            return 0, inf, -inf, 0
    
        dfs(root)
        return result
# @lc code=end