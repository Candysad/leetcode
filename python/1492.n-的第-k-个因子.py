#
# @lc app=leetcode.cn id=1492 lang=python3
#
# [1492] n 的第 k 个因子
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n+1//2):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        if count == k-1:
            return n
        return -1
# @lc code=end

