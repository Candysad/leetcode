#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from collections import defaultdict
from heapq import *
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        queue = [(-count[n], n) for n in count]
        heapify(queue)
        
        return [heappop(queue)[1] for _ in range(k)]
# @lc code=end

