#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from itertools import combinations
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(combinations(range(1, n+1), k))
        
        start = 0
        for i in range(k):
            start |= 1 << i
            
        result = []
        nums = list(range(1, n+1))
        for i in range(start, 2**n):
            if i.bit_count() != k: continue
            
            t = []
            for j in range(n):
                if(i >> j) & 1:
                    t.append(nums[j])
            result.append(t)
        
        return result
# @lc code=end