#
# @lc app=leetcode.cn id=2476 lang=python3
#
# [2476] 二叉搜索树最近节点查询
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        '''
        二分查找
        直接在树上每次查找一个值累计可能超时
        先把树变成有序数组
        '''
        
        array = []
        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            array.append(node.val)
            dfs(node.right)
        dfs(root)
        
        result = []
        for q in queries:
            t = bisect_left(array, q)
            ans = [-1, -1]
            if t != len(array):
                ans[1] = array[t]
                if array[t] == q:
                    result.append([q, q])
                    continue
            if t != 0:
                ans[0] = array[t-1]
            result.append(ans)
        
        return result
# @lc code=end

