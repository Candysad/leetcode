#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p and q is None) or (p is None and q):
            return False
        
        def dfs(node1, node2):
            if node1.val != node2.val:
                return False

            t1 = False
            if node1.left and node2.left:
                t1 = dfs(node1.left, node2.left)
            elif node1.left is None and node2.left is None:
                t1 = True
            
            if t1:
                t2 = False
                if node1.right and node2.right:
                    t2 = dfs(node1.right, node2.right)
                elif node1.right is None and node2.right is None:
                    t2 = True
                return t1 & t2
            else:
                return False
        
        return dfs(p, q)                  
# @lc code=end

