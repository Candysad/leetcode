#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        两次遍历
        第一次记录父节点和层数
        '''
        # bfs
        # queue = [root]
        # layer = 0
        # while queue:
        #     t = queue
        #     queue = []
        #     for tt in t:
        #         tt.layer = layer
        #         if tt.left:
        #             tt.left.head = tt
        #             queue.append(tt.left)
        #         if tt.right:
        #             tt.right.head = tt
        #             queue.append(tt.right)
        #     layer += 1
        
        # # 从给定位置往上找
        # while p != q:
        #     if p.layer > q.layer:
        #         p = p.head
        #     else:
        #         q = q.head
        # return p
    
        '''
        二叉搜索树
        父节点一定在大小上在给定节点中间
        不存在的话就是两者中高的那一个
        '''
        node = root
        t = [p.val, q.val] if p.val < q.val else [q.val, p.val]
        while node != p and node != q:
            if node.val > t[1]:
                node = node.left
            elif node.val < t[0]:
                node = node.right
            else:
                break
        return node
        
            
# @lc code=end

