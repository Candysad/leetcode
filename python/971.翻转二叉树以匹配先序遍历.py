#
# @lc app=leetcode.cn id=971 lang=python3
#
# [971] 翻转二叉树以匹配先序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        if root.val != voyage[0]:
            return [-1]
        
        result = []
        n = len(voyage)
        def dfs(node, i):
            if node is None:
                return i
            
            if node.val != voyage[i]:
                return -1
            
            # 左右
            t = dfs(node.left, i+1)
            if t != -1:
                t = dfs(node.right, t)
                if t != -1:
                    return t
            
            # 右左
            t = dfs(node.right, i+1)
            if t != -1:
                t = dfs(node.left, t)
                if t != -1:
                    result.append(node.val)
                    return t
            
            return -1

        t = dfs(root, 0)
        return result if t!= -1 else [-1]
# @lc code=end