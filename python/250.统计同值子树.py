#
# @lc app=leetcode.cn id=250 lang=python3
#
# [250] 统计同值子树
#
from math import inf
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None: return -1, 0, 0
            
            leftt, leftv, leftc = dfs(node.left)
            rightt, rightv, rightc = dfs(node.right)
            
            if leftt < 1 and rightt < 1:
                if leftt == 0 and rightt == 0:
                    if leftv == rightv == node.val:
                        return 0, leftv, leftc + rightc + 1
                    else:
                        return 1, 0, leftc + rightc
                elif leftt == -1 and rightt == -1:
                    return 0, node.val, 1
                else:
                    v = leftv if leftt == 0 else rightv
                    c = leftc if leftt == 0 else rightc
                    if v == node.val:
                        return 0, v, c + 1
                    else:
                        return 1, 0, c
            else:
                return 1, 0, leftc + rightc
        
        return dfs(root)[2]
# @lc code=end