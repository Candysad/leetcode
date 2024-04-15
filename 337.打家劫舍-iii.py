#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, last:bool):
            if node is None:
                return 0
            
            if last:# 上一个偷了，这里只能不偷
                return dfs(node.left, False) + dfs(node.right, False)
            else: # 上一个没偷，这里可以偷也可以不偷
                t = dfs(node.left, True) + dfs(node.right, True) + node.val
                bt = dfs(node.left, False) + dfs(node.right, False)
                return max(t, bt)

        return dfs(root, False)      
# @lc code=end

