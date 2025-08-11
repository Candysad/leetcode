#
# @lc app=leetcode.cn id=1552 lang=python3
#
# [1552] 两球之间的磁力
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        
        def check(num):
            res = m - 1
            last = position[0]
            for i in range(n):
                if position[i] - last >= num:
                    res -= 1
                    if res == 0: return True
                    
                    last = position[i]
            return False

        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = left + ((right - left) >> 1)
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
# @lc code=end