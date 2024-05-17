#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        一次递归找出
        '''
        result = root
        def dfs(node):
            '''
            每层返回目标节点是否在自己下面
            第一个两个节点都出现的地方就是答案
            '''
            if node is None:
                return False, False

            
            pl, ql = dfs(node.left)
            if pl and ql:
                return False, False
            
            pr, qr = dfs(node.right)
            if pr and qr:
                return False, False
            
            pa = node == p
            qa = node == q
            pa |= pl | pr
            qa |= ql | qr
            
            if pa and qa:
                nonlocal result
                result = node
                return False, False
            
            return pa, qa 
            
        dfs(root)
        return result
    
        '''
        分别找出前缀然后匹配
        '''
        # pre1 = []
        # def find1(node):
        #     if node is None:
        #         return False
        #     if node == p:
        #         pre1.append(p)
        #         return True
            
        #     pre1.append(node)
            
        #     if find1(node.left):
        #         return True
        #     if find1(node.right):
        #         return True
            
        #     pre1.pop()
        #     return False

        # pre2 = []
        # def find2(node):
        #     if node is None:
        #         return False
        #     if node == q:
        #         pre2.append(q)
        #         return True
            
        #     pre2.append(node)
            
        #     if find2(node.left):
        #         return True
        #     if find2(node.right):
        #         return True
            
        #     pre2.pop()
        #     return False

        # find1(root)
        # find2(root)
        # # print(pre1)
        # # print(pre2)
        
        # i = 0
        # while i < min(len(pre1), len(pre2)):
        #     if pre1[i] != pre2[i]:
        #         return pre1[i-1]
        #     i += 1
        
        # if i < len(pre1):
        #     return pre1[i-1]
        # else:
        #     return pre2[i-1]

# @lc code=end

