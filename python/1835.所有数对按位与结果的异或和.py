#
# @lc app=leetcode.cn id=1835 lang=python3
#
# [1835] 所有数对按位与结果的异或和
#
from operator import xor
from functools import reduce
# @lc code=start
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        t1 = reduce(xor, arr1)
        t2 = reduce(xor, arr2)
        return t1 & t2
# @lc code=end