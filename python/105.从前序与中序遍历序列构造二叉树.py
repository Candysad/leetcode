#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):  
            nowhead = preorder[0]
            node = TreeNode(nowhead)
            if len(preorder) == 1:
                return node
            
            i = inorder.index(nowhead)
            node.left = dfs(preorder[1:i+1], inorder[0:i]) if i != 0 else None
            node.right = dfs(preorder[i+1:], inorder[i+1:]) if i!= len(inorder)-1 else None
            return node
        
        return dfs(preorder, inorder)
# @lc code=end

