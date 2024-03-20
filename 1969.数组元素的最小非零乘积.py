 #
# @lc app=leetcode.cn id=1969 lang=python3
#
# [1969] 数组元素的最小非零乘积
#

# @lc code=start
def binpow(base, exponent, mod):
    '''
    用二分实现带取模的快速幂
    根据乘法性质在过程中取模
    幂可以按照指数的二进制拆分成多个幂 3^13 = 3^(1101)  = 3^8 * 3^4 * 3^1
    底数从小到大平方，当前指数的二进制位是1就乘在答案里
    '''
    base = base % mod
    result = 1
    while exponent:
        if exponent & 1: # 指数每次右移，按当前最小位判断原来指数这里要不要乘
            result = result *  base % mod
        base = base * base % mod
        exponent >>= 1
    return result
            
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        '''
        数学题
        减少最小的，总体乘积减少的最多
        增大最大的，总体乘积增加的最少
        最后变成一堆1和2^{p-1}-1 个 2^p-2，和最开始最大的 2^p-1
        
        带取模的快速幂
        要求取模，在计算幂时实现
        '''
        if p == 1:
            return 1
        mod = 10**9 + 7
         
        return binpow(2**p-2, 2**(p-1)-1, mod) * (2**p-1) % mod
# @lc code=end

