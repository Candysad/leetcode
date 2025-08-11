#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        
        def dfs(left, right):
            if left > right:
                return None
            
            mid = left + ((right - left) >> 1)
            now = TreeNode(nums[mid])
            now.left = dfs(left, mid - 1)
            now.right = dfs(mid + 1, right)
            return now
        
        return dfs(0, n-1)
# @lc code=end