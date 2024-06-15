#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        l1, l2 = len(a), len(b)
        if l1 > l2:
            a, b = b, a
            l1, l2 = l2, l1
        
        if l1 < l2: return l2
        if a == b:return -1
        return l1
# @lc code=end