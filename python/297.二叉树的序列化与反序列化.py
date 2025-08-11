#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    
    def serialize(self, root):
        if root is None: return ''
        
        result = []
        queue = [root]
        while queue:
            t = queue
            queue = []
            
            for node in t:
                if node:
                    result.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append('null')
        
        for i in range(len(result)-1 , -1, -1):
            if result[i] != 'null':
                break
        return ','.join(result[:i+1])

    def deserialize(self, data):
        if data == '': return None
        data = data.split(',')
        
        root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        n = len(data)
        while i < n:
            t = []
            for node in queue:
                if i == n: break
                if data[i] != "null":
                    node.left = TreeNode(int(data[i]))
                    i += 1
                    t.append(node.left)
                else:
                    i += 1

                if i == n: break
                if data[i] != "null":
                    node.right = TreeNode(int(data[i]))
                    i += 1
                    t.append(node.right)
                else:
                    i += 1
            queue = t
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

