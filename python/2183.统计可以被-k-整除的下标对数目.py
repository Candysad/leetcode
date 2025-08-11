#
# @lc app=leetcode.cn id=2183 lang=python3
#
# [2183] 统计可以被 K 整除的下标对数目
#
from math import gcd
from collections import Counter
# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        factors = set()
        for i in range(1, k+1):
            if i * i > k:break
            
            if k % i == 0:
                factors.add(i)
                factors.add(k // i)
        factorlist = list(factors)
        
        result = 0
        counter = Counter()
        for num in nums:
            g = gcd(num, k)
            if g in factors:
                result += counter[k // g]
            
            for factor in factorlist:
                if num % factor == 0:
                    counter[factor] += 1
        return result
# @lc code=end