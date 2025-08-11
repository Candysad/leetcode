#
# @lc app=leetcode.cn id=1427 lang=python3
#
# [1427] 字符串的左右移
#
from collections import deque
# @lc code=start
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        for t, l in shift:
            l %= n
            if t == 0:
                s = s[l:] + s[:l]
            else:
                s = s[:-l] + s[-l:]
        return s  
# @lc code=end