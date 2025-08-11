#
# @lc app=leetcode.cn id=545 lang=python3
#
# [545] 二叉树的边界
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        result = [root.val]
        
        def dfs(node, lr): # lr 0 最左； 1 中间； 2 最右
            if node is None: return
            
            if lr == 0:
                result.append(node.val)
                if node.left:
                    dfs(node.left, 0)
                    dfs(node.right, 1)
                else:
                    dfs(node.right, 0)
            
            elif lr == 1:
                if node.left is None and node.right is None:
                    result.append(node.val)
                else:
                    dfs(node.left, 1)
                    dfs(node.right, 1)
            
            elif lr == 2:
                if node.right:
                    dfs(node.left, 1)
                    dfs(node.right, 2)
                    
                else:
                    dfs(node.left, 2)
                result.append(node.val)
        
        dfs(root.left, 0)
        dfs(root.right,2)
        return result
# @lc code=end