#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        不用递归
        先遍历左边再回来遍历自己然后再遍历右边
        需要存一下自己然后之后再拿出来 栈
        '''
        if root is None:
            return []
        
        stack = []
        result = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            if node is None:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result
        
        

        '''
        中序遍历：先自己再左右
        '''
        # if root is None:
        #     return []
        
        # result = []
        # def dfs(node):
        #     nonlocal result
            
        #     if node.left is not None:
        #         dfs(node.left)
            
        #     result.append(node.val)
            
        #     if node.right is not None:
        #         dfs(node.right)
        
        # dfs(root)
        # return result
# @lc code=end

