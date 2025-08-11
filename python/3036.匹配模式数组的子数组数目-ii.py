#
# @lc app=leetcode.cn id=3036 lang=python3
#
# [3036] 匹配模式数组的子数组数目 II
#
from itertools import pairwise
# @lc code=start
class Solution:
    def countMatchingSubarrays(self, nums: List[int], p: List[int]) -> int:
        def gen_next(p):
            n = len(p)
            next = [-1] * n
            
            for i in range(1, n):
                last = next[i-1]
                while last > -1 and p[last + 1] != p[i]:
                    last = next[last]
                if p[last + 1] == p[i]:
                    next[i] = last + 1
            return next

        
        s = []
        for a, b in pairwise(nums):
            if a == b:
                s.append(0)
            elif a > b:
                s.append(-1)
            else:
                s.append(1)
        
        next = gen_next(p)
        result = 0
        i, j = 0, 0
        sn, pn = len(s), len(p)
        while i < sn:
            if s[i] == p[j]:
                i += 1
                j += 1
                if j == pn:
                    result += 1
                    j = next[j-1] + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = next[j-1] + 1
        return result
# @lc code=end