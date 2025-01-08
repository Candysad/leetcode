#
# @lc app=leetcode.cn id=298 lang=python3
#
# [298] 二叉树最长连续序列
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        result = 1
        def dfs(node, pre):
            nonlocal result
            if node.left is None and node.right is None:
                result = max(result, pre)
                return
            
            if node.left:
                if node.left.val == node.val + 1:
                    dfs(node.left, pre+1)
                else:
                    result = max(result, pre)
                    dfs(node.left, 1)
            if node.right:
                if node.right.val == node.val + 1:
                    dfs(node.right, pre+1)
                else:
                    result = max(result, pre)
                    dfs(node.right, 1)
        dfs(root, 1)
        return result
# @lc code=end