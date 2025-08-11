#
# @lc app=leetcode.cn id=1261 lang=python3
#
# [1261] 在受污染的二叉树中查找元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    '''
    BFS + 表
    BFS理清树
    查表
    '''
    def __init__(self, root: Optional[TreeNode]):
        self.num_dict = {0:True}
        root.val = 0
        queue = [root]
        while queue:
            t = queue
            queue = []
            for node in t:
                t_val = 2 * node.val + 1
                if node.left:
                    node.left.val = t_val
                    queue.append(node.left)
                    self.num_dict[t_val] = True
                if node.right:
                    node.right.val = t_val + 1
                    queue.append(node.right)
                    self.num_dict[t_val+1] = True

    def find(self, target: int) -> bool:
        return self.num_dict.get(target, False)



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

