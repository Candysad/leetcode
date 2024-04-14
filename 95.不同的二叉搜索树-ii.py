#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
from functools import cache
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        '''
        改成递归可读性更好
        时间和dp一毛一样
        '''
        @cache
        def dfs(left:int , right:int):
            if right == left - 1 or left == right + 1:
                return [None]
            if left == right:
                return [TreeNode(val=left)]
            
            result = []
            for mid in range(left, right+1):
                for l in dfs(left, mid-1):
                    for r in dfs(mid+1, right):
                        result.append(TreeNode(mid, l, r))
            return result

        return dfs(1, n)
        
        
        '''
        dp[i][j] 表示节点 [i...j] 组成的所有二叉搜索树（存头节点）
        dp[i][j] 应该由 [i...k...j] 中的k作为头节点，然后以[i...k-1]为左侧，以[k+1...j] 为右侧
            即 dp[i][j] = k
                          -left->  dp[i][k-1]
                          -right-> dp[k+1][j]
                          
        状态转的条件太多，循环层数太多，不好维护
        其实内存和时间和递归是一样的
        '''
        # dp = [[[None]]* (n+2) for _ in range(n+2)] # 两端多出来作为空的叶子节点
        
        # # 区间长度，找dp[1][3]时必须先找过dp[1][2] 和 dp[2][3]
        # for l in range(1, n+1): 
        #     # 区间左侧，区间右侧下标为 i+l-1
        #     for i in range(1, n-l+2): # 左侧只从1开始，dp[i][0] 意味着左侧空节点
        #         j = i + l -1
        #         dp[i][j] = []
        #         # 在[i, i+l-1]中作为头节点遍历
        #         for mid in range(i, j+1): # 对于mid-1 和 mid+1 在两侧超出去的情况，会访问到 None 作为空的叶子节点
        #             # 遍历左侧可行的子树
        #             for left in dp[i][mid-1]:
        #                 # 遍历右侧子树
        #                 for right in dp[mid+1][j]:
        #                     dp[i][j].append(TreeNode(mid, left, right))
        # return dp[1][n]
# @lc code=end

