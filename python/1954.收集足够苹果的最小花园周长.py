#
# @lc app=leetcode.cn id=1954 lang=python3
#
# [1954] 收集足够苹果的最小花园周长
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def apples(k):
            # side = 12 * k * k
            # inside = 2 * k * (k+1) * (2*k+1) - side
            return  2 * k * (k+1) * (2*k+1)
        
        left, right = 0, 100000
        k = -1
        while left <= right:
            # print(left, apples(left))
            # print(right, apples(right))
            mid = (left + right) // 2
            n = apples(mid)
            # print("mid: ", mid, n)
            if n == neededApples:
                k = mid
                break
            elif n < neededApples:
                left = mid + 1
            else:
                right = mid - 1
            
            # print("============")
        k = left if k == -1 else k
        return 8 * k
# @lc code=end

