#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        bfs
        '''
        sum_ = 0
        queue = [root]
        while queue:
            now = queue
            queue = []
            for node in now:
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    if node.val >= low and node.val <= high:
                        sum_ += node.val
        return sum_
                
                    
# @lc code=end

