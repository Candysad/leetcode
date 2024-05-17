#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
N = 5000000
is_prime = [0, 0, 1] + [0 if i % 2 else 1 for i in range(N-3)]
for i in range(2, isqrt(N)+1):
    if is_prime[i]:
        for j in range(i*i, N, i):
            is_prime[j] = 0

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
            return sum(is_prime[:n])
        

# @lc code=end

