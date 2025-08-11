#
# @lc app=leetcode.cn id=1735 lang=python3
#
# [1735] 生成乘积数组的方案数
#
from collections import defaultdict
from functools import cache
from copy import deepcopy
from math import comb
# @lc code=start
pri = []
n = 10000
not_prime = [False] * (n+1)

for i in range(2, n + 1):
    if not not_prime[i]:
        pri.append(i)
        
    for pri_j in pri:
        if i * pri_j > n:
            break
        not_prime[i * pri_j] = True
        if i % pri_j == 0:
            break

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        '''
        插板法
        相同类别元素分成指定的组数，每组至少一个元素，求所有可能的分组情况，相同情况的不同顺序算不同分组
        在他们中间插入隔板形成分组
        '''
        mod = 10**9 + 7
        @cache
        def factors(i):
            if i == 1: return defaultdict(int)
            for p in pri:
                if i % p == 0:
                    tmp = deepcopy(factors(i//p))
                    tmp[p] += 1
                    return tmp

        @cache
        def c(m, n):
            return comb(m, n) % mod
        
        result = []
        for n, k in queries:
            t = 1
            fs = factors(k)
            for ps in fs.values():
                t *= c(ps+n-1, n-1)
                t %= mod
            result.append(t)
        return result
# @lc code=end