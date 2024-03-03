#
# @lc app=leetcode.cn id=2583 lang=python3
#
# [2583] 二叉树中的第 K 大层和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        '''
        DFS
        深度优先
        时间换空间
        '''
        # # def print_layer(node):
        # #     if node == None:
        # #         print("None")
        # #         return
        # #     print(node.val, node.layer)
        # #     print_layer(node.left)
        # #     print_layer(node.right)
        
        # def dfs_for_layer_count(node, layer:int):
        #     # 至少有两个节点，不需要在一开始判断空节点
        #     node.layer = layer
            
        #     left_depth = -1
        #     right_depth = -1
        #     if node.left != None:
        #         left_depth = dfs_for_layer_count(node.left, layer=layer+1)
        #     if node.right != None:
        #         right_depth = dfs_for_layer_count(node.right, layer=layer+1)
                
        #     t = left_depth if left_depth > right_depth else right_depth
        #     t = node.layer if node.layer > t else t
        #     return t
            
        # depth = dfs_for_layer_count(root, 0)
        # if depth < k-1:
        #     return -1
        # layers = [0 for _ in range(depth+1)]
        
        # def dfs_count(node):
        #     layers[node.layer] += node.val
            
        #     if node.left != None:
        #         dfs_count(node.left)
        #     if node.right != None:
        #         dfs_count(node.right)
        
        # dfs_count(root)
        # layers.sort()
        
        # # print_layer(root)
        # # print(layers)
        # # print(depth)
        
        # return layers[-k]
    
        '''
        BFS
        队列实现一次遍历
        空间换时间
        '''
        layers_sum = []
        queue = [root]
        
        while queue:
            layer_sum = 0
            layer = queue
            queue = []
            for node in layer:
                layer_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            layers_sum.append(layer_sum)
        
        layers_sum.sort()
        return -1 if len(layers_sum) < k else layers_sum[-k]
# @lc code=end

