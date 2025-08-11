#
# @lc app=leetcode.cn id=2096 lang=python3
#
# [2096] 从二叉树一个节点到另一个节点每一步的方向
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path1, path2 = [[root.val, '']], [[root.val, '']]
        node1, node2 = False, False
        parent = -1
        def search(node):
            nonlocal node1, node2, parent
            if node is None:
                return False, False

            n1, n2 = False, False
            if node.val == startValue:
                node1 |= True
                n1 = True
            if node.val == destValue:
                node2 |= True
                n2 = True

            leftnode1, leftnode2 = False, False
            if node.left is not None:
                if not node1:
                    path1.append([node.left.val, 'L'])
                if not node2:
                    path2.append([node.left.val, 'L'])
                if not node1 or not node2:
                    leftnode1, leftnode2 = search(node.left)
                    node1 |= leftnode1
                    node2 |= leftnode2
                    if not node1:
                        path1.pop()
                    if not node2:
                        path2.pop()
            
            rightnode1, rightnode2 = False, False
            if node.right is not None:
                if not node1:
                    path1.append([node.right.val, 'R'])
                if not node2:
                    path2.append([node.right.val, 'R'])
                if not node1 or not node2:
                    rightnode1, rightnode2 = search(node.right)
                    node1 |= rightnode1
                    node2 |= rightnode2
                    if not node1:
                        path1.pop()
                    if not node2:
                        path2.pop()
            
            n1 |= leftnode1 or rightnode1
            n2 |= leftnode2 or rightnode2
            if parent == -1 and n1 and n2:
                parent = node.val
            return n1, n2
        
        search(root)
        path = []
        for node in path1[::-1]:
            if node[0] != parent:
                path.append('U')
            else: break
        for i, node in enumerate(path2):
            if node[0] == parent: break
        for node in path2[i+1:]:
            path.append(node[1])
        
        return ''.join(path)                  
# @lc code=end