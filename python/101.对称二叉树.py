#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        bfs
        '''
        queue = [root]
        while queue:
            t = queue
            # print(t)
            left, right = 0, len(t) - 1
            while left < right:
                if t[left] is None or t[right] is None:
                    if t[left] is not t[right]:
                        return False
                elif t[left].val != t[right].val:
                    return False
                left += 1
                right -= 1
            
            queue = []
            for node in t:
                if node is not None:
                    queue.append(node.left)
                    queue.append(node.right)
        
        return True
    
# @lc code=end

