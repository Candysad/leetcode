#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        path = []
        def dfs(node):
            path.append(node.val)
            if node.left is None and node.right is None:
                nonlocal result
                result += int(str(''.join([str(c) for c in path])))

            if node.left is not None:
                dfs(node.left)
            
            if node.right is not None:
                dfs(node.right)
            
            path.pop()
            
        dfs(root)
        return result
# @lc code=end