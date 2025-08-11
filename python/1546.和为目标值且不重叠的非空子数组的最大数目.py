#
# @lc app=leetcode.cn id=1546 lang=python3
#
# [1546] 和为目标值且不重叠的非空子数组的最大数目
#
from collections import defaultdict
from itertools import accumulate
from bisect import bisect_left
# @lc code=start
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # table = defaultdict(list)
        # table[0].append(0)
        # pres = [0] * (n+1)
        # for i, pre in enumerate(accumulate(nums)):
        #     table[pre].append(i+1)
        #     pres[i+1] = pre
        
        # dp = [0] * (n+1)
        # for i in range(n+1):
        #     dp[i] = dp[i-1]
        #     pre = pres[i]
        #     if table[pre - target]:
        #         ti = bisect_left(table[pre - target], i) - 1
        #         if ti >= 0:
        #             prei = table[pre - target][ti]
        #             dp[i] = max(dp[i], dp[prei] + 1)

        # return dp[-1]
        
        result = 0
        pres = set([0])
        for pre in accumulate(nums):
            if pre - target in pres:
                pres.clear()
                result += 1
            pres.add(pre)
        return result
# @lc code=end