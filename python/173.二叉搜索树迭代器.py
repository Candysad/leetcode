#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        def dfs(node):
            if node is None: return
            if node.left:
                dfs(node.left)
            
            self.stack.append(node.val)
            
            if node.right:
                dfs(node.right)
        dfs(root)
        self.i = 0


    def next(self) -> int:
        t = self.stack[self.i]
        self.i += 1
        return t

    def hasNext(self) -> bool:
        return self.i < len(self.stack)

# @lc code=end