#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        处理越界和符号
        用除数的2次幂的倍数做加法因子
        找被除数里分别由哪些因子相加得到
        被除数 =  除数 * 2^(t1+t2...)
        本质上是一种二分法
        '''
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0
        
        # 符号
        # 把两边都改成负数
        # 正数绝对值范围小一点可能越界
        sign = 1
        if dividend > 0:
            dividend = -dividend
            sign = -sign
        if divisor > 0:
            divisor = -divisor
            sign = -sign
        
        # 因为都是负数所以反过来比较
        # 用数组存一下所有2的幂倍的除数
        powers = [divisor]
        # 最后一个如果放的是更大的，可能会越界
        while dividend - powers[-1] <= powers[-1]: # 直接比新的两倍也可能越界
                                                   # 要放在左边
            powers.append(powers[-1] + powers[-1])
        
        result = 0
        # 在记录中每次将最大的部分减去
        # 剩下的被除数一定在更小的除数倍数中
        # 合计2的幂即可
        for i in range(len(powers) - 1, -1, -1):
            if dividend <= powers[i]:
                result += 1 << i
                dividend -= powers[i]
        return sign * result # 带上符号
        
        
# @lc code=end

