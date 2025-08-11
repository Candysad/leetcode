#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#
from math import lcm
from bisect import bisect_left
# @lc code=start
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10 ** 9 + 7
        def check(num):
            return num // a + num // b - num // lcm(a,b)
        
        left, right = 0, min(a,b) * n
        while left < right:
            mid = left + ((right - left) >> 1)
            c = check(mid)
            if c >= n:
                right = mid
            else:
                left = mid + 1
            
        return left % mod
# @lc code=end