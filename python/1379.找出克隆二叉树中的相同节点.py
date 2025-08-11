#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        '''
        俩树完全一样
        值还不重复
        那就遍历到目标值就停下来
        
        如果有重复值，那就和original一起遍历，当original里找到target时，cloned也停下来
        '''
        queue = [cloned]
        while queue:
            t = queue
            queue = []
            for node in t:
                if node == None:
                    continue
                if node.val == target.val:
                    return node
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        return None 
        
# @lc code=end

