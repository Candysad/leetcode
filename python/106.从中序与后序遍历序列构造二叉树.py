#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        值唯一
        '''
        n = len(inorder)
        def dfs(il, ir, pl, pr):
            if il == ir:
                return TreeNode(inorder[il])
            if il > ir:
                return None
            
            node = TreeNode(postorder[pr])
            ip = inorder.index(postorder[pr])
            
            node.left = dfs(il, ip-1, pl, pl + ip-il-1)
            node.right = dfs(ip+1, ir, pl + ip-il, pr-1)
            return node

        return dfs(0, n-1, 0, n-1)
# @lc code=end