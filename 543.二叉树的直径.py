#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            '''
            这里面算的都是路径上的节点个数，最后 -1 就是路径长度了
            '''
            if node is None:
                return 0, 0
            
            # 左子树里有个大的
            leftdown, leftup = dfs(node.left)
            
            # 右子树里有个大的
            rightdown, rightup = dfs(node.right)
            
            # 返回下面某层有个大的
            # 对当前节点的上层来说，可能是当前节点更下面有个大的，或者是经过当前节点但是不往上有个大的
            down = max(leftdown, rightdown, leftup + rightup + 1) # +1 是带上当前节点
            
            # 还要返回经过当前节点往上走的最大的
            up = max(leftup, rightup) + 1
            
            return down, up
        
        return max(dfs(root))-1
        
# @lc code=end

