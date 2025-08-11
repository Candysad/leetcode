#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        中序遍历+计数，数够了就找到了
        '''
        result = -1
        c = 0
        
        def dfs(node):
            nonlocal c, result
            if node is None:
                return 0
            
            if result != -1:
                return 
            
            left = dfs(node.left)
            
            c += 1
            if c == k:
                result = node.val
            
            right = dfs(node.right)

        dfs(root)
        return result
# @lc code=end

