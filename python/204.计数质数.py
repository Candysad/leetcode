#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
from math import isqrt
# @lc code=start
# 线性筛
N = 5* 10**6 + 1
pri = []
ispri = [0, 0] + [1] * N
for i in range(2, N):
    if ispri[i]:
        pri.append(i)
        
    for j in pri:
        if i * j >= N:
            break
        ispri[i*j] = 0

        if i % j == 0:
            break

class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        埃氏筛
        提前算好可以节省重复查的时间
        数数
        '''
        if n <= 2: 
            return 0
        else:
            return sum(ispri[:n])
# @lc code=end

