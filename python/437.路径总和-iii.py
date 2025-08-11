#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
from math import inf
from collections import defaultdict
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        前缀和+回溯
        '''
        result = 0
        pre_sum = [0] # 按顺序记录
        pre_set = defaultdict(int) # 方便查找
        pre_set[0] = 1
        def dfs(node):
            if node is None:
                return

            now = node.val + pre_sum[-1]
            
            # 找前面有没有  
            if now-targetSum in pre_set:
                nonlocal result
                result += pre_set[now-targetSum]
            
            # 放入当前
            pre_sum.append(now)
            pre_set[now] += 1
            
            # 进入下层
            dfs(node.left)
            dfs(node.right)
            
            #回溯退掉自己
            pre_sum.pop()
            pre_set[now] -= 1
        
        dfs(root)
        return result
        
        '''
        加vis防止重复递归
        '''
        # result = 0
        # vis = set()
        # def dfs(node, pre):
            
        #     if node is None:
        #         return
        #     now = pre + node.val if pre != inf else node.val
        #     if now == targetSum:
        #         nonlocal result
        #         result += 1
            
            
        #     dfs(node.left, now)
        #     dfs(node.right, now)
            
        #     if node not in vis:
        #         dfs(node.left, inf)
        #         dfs(node.right, inf)
            
        #     vis.add(node)
            
        # dfs(root, inf)
        # return result
# @lc code=end

