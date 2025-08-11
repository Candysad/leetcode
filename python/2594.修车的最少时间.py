#
# @lc app=leetcode.cn id=2594 lang=python3
#
# [2594] 修车的最少时间
#
from collections import Counter
from math import sqrt, floor
# @lc code=start
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        counter = Counter(ranks)
        rs = counter.keys()
        def check(num):
            result = 0
            for r in rs:
                c = floor(sqrt(num // r))
                result += c * counter[r]
                if result >= cars: return True
            return False
        
        left, right = 1, max(rs) * cars * cars
        while left < right:
            mid = left + ((right - left) >> 1)
            c = check(mid)
            if c:
                right = mid
            else:
                left = mid + 1
        
        return left
# @lc code=end