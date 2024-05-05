#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#
# @lc code=start
from heapq import *
# @lc code=start
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        r = sorted(zip(wage, quality), key=lambda x: x[0] / x[1])
        queue = [-q for _, q in r[:k]]
        heapify(queue)
        sumq = -sum(queue)
        result = sumq * r[k-1][0] / r[k-1][1]
               
        for w, q in r[k:]:
            if q < -queue[0]:
                sumq += q + heapreplace(queue, -q)
                result = min(result, sumq * w / q)
        return result
# @lc code=end

