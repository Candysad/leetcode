#
# @lc app=leetcode.cn id=1802 lang=python3
#
# [1802] 有界数组中指定下标处的最大值
#

# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = index, n - 1 - index
        
        def check(x):
            leftlimit = min(x, l)
            rightlimit = min(x, r)
            tl = (x + x - leftlimit) * (leftlimit + 1) // 2
            tr = (x + x - rightlimit) * (rightlimit + 1) // 2
            return tl + tr - x

        left, right = 1, maxSum - n
        while left <= right:
            mid = left + ((right - left) >> 1)
            if check(mid) <= maxSum - n:
                left = mid + 1
            else:
                right = mid - 1
        return right + 1
# @lc code=end