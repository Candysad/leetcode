#
# @lc app=leetcode.cn id=1120 lang=python3
#
# [1120] 子树的最大平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        result = 0
        def dfs(node):
            if node is None: return 0, 0
            
            leftsum, leftc = dfs(node.left)
            rightsum, rightc = dfs(node.right)
            nowsum = node.val + leftsum + rightsum
            nowc = leftc + rightc + 1
            
            nonlocal result
            result = max(result, nowsum / nowc)
            
            return nowsum, nowc
        
        dfs(root)
        return result
# @lc code=end