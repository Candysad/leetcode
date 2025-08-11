#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        '''
        叶子节点#得个数应该为非叶子节点出现个数+1
        提前出现叶子节点也算错
        '''
        stack = 1
        n = len(preorder)
        preorder = preorder.split(",")
        for i, node in enumerate(preorder):
            if node != '#':
                stack += 1
            else:
                stack -= 1
            if stack == 0 and i != n-1:
                return False
        return True if stack == 0 else False
# @lc code=end

