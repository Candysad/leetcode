#
# @lc app=leetcode.cn id=2400 lang=python3
#
# [2400] 恰好移动 k 步到达某一位置的方法数目
#
from functools import cache
from math import comb
# @lc code=start
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9 + 7
        d = abs(endPos - startPos) # 起点终点的距离，必要的靠近次数
        if k < d or (k-d) % 2 != 0:
            return 0
        t = (k - d) // 2
        return comb(k, t) % mod

        # mod = 10**9 + 7
        # d = abs(endPos - startPos) # 起点终点的距离，必要的靠近次数
        # if k < d or (k-d) % 2 != 0:
        #     return 0
        
        # ld = (k - d) // 2 # 剩余要溜达的步数//2
        #                  # 因为最终要回到终点，溜达出去还得溜达回来
        #                  # 记录总的溜达出去又回来的次数 
        # # length = endPos + t - (startPos - t)
        # # length = endPos - startPos + 2 * t

        # @cache
        # def dfs(i, k):
        #     if abs(endPos - i) > k:
        #         return 0

        # return dfs(d, ld)
# @lc code=end

