#
# @lc app=leetcode.cn id=314 lang=python3
#
# [314] 二叉树的垂直遍历
#
from collections import defaultdict
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        table = defaultdict(list)
        table[0].append(root.val)
        
        queue = [(root,0)]
        while queue:
            t = queue
            queue = []
            for node, i in t:
                if node.left:
                    table[i-1].append(node.left.val)
                    queue.append((node.left, i-1))
                if node.right:
                    table[i+1].append(node.right.val)
                    queue.append((node.right, i+1))
        result = []
        for key in sorted(list(table.keys())):
            result.append(table[key])
        return result
# @lc code=end