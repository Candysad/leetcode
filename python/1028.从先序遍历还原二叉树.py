#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        table = defaultdict(int)
        root = None
        def insert(n, num):
            if n == 0:
                t = TreeNode(num)
                table[0] = t
                nonlocal root
                root = t
            
            else:
                p = table[n-1]
                if p.left == None:
                    p.left = TreeNode(num)
                    table[n] = p.left
                else:
                    p.right = TreeNode(num)
                    table[n] = p.right

        lasti = 0
        n = 0
        for i, c in enumerate(traversal):
            if traversal[lasti] == '-':
                if c == '-': continue
                else:
                    n = i - lasti
                    lasti = i
            else:
                if c == '-':
                    num = int(traversal[lasti:i])
                    insert(n, num)
                    lasti = i
                else: continue
        num = int(traversal[lasti:])
        insert(n, num)
        
        return root
# @lc code=end

