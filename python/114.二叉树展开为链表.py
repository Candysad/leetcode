#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        先把左子树捋直了，返回左侧的末尾节点
        再把右子树捋直了，返回右侧的末尾节点
        把左子树放在自己右边，左子树末尾接上右子树头，向上返回右子树末尾
        '''
        if root is None:
            return None
        
        def dfs(node):
            left = node.left
            if left:
                lefttail = dfs(node.left)
            
            right = node.right
            if right:
                righttail = dfs(node.right)
            
            
            if left and right:
                node.left = None
                node.right = left
                lefttail.right = right
                return righttail
            
            elif left:
                node.left = None
                node.right = left
                return lefttail
            
            elif right:
                return righttail
            
            else:
                return node
        
        dfs(root)
        return root

# @lc code=end

