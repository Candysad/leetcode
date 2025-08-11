#
# @lc app=leetcode.cn id=366 lang=python3
#
# [366] 寻找二叉树的叶子节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            queue =[]
            if root.left:
                queue.append((root.left, root, 0))
            if root.right:
                queue.append((root.right, root, 1))
            
            result = []
            while queue:
                t = queue
                queue = []
                for node, p, lr in t:
                    if node.left is None and node.right is None:
                        result.append(node.val)
                        if lr: p.right = None
                        else: p.left = None
                    
                    if node.left:
                        queue.append((node.left, node, 0))
                    if node.right:
                        queue.append((node.right, node, 1))
            
            return result

        result = []
        while root.left or root.right:
            result.append(bfs(root))
        result.append([root.val])
        return result
# @lc code=end