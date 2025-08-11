#
# @lc app=leetcode.cn id=2064 lang=python3
#
# [2064] 分配给商店的最多商品的最小值
#
# @lc code=start
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        
        def check(num):
            result = 0
            for q in quantities:
                if q % num == 0:
                    result += q // num
                else:
                    result += q // num + 1
            return result <= n
        
        left, right = 1, max(quantities)
        while left <= right:
            mid = left + ((right - left) >> 1)
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return right
# @lc code=end