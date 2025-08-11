#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#
from bisect import *
from math import lcm
# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        nums = [a, b, c]
        def check(m: int) -> bool:
            cnt = 0
            for i in range(1, 1 << len(nums)):  # 用位枚举所有非空子集
                lcm_res = 1  # 计算子集 LCM
                for j, x in enumerate(nums):
                    if i >> j & 1: # 看这个数当前子集选没选
                        lcm_res = lcm(lcm_res, x) # 更新最小公倍数
                        if lcm_res > m:  # 太大了,超过当前查找范围 m
                            break
                else:  # 中途没有 break
                    # 用1的个数计子集中的数字个数
                    cnt += m // lcm_res if i.bit_count() % 2 else -(m // lcm_res)
            # n为要找的计数，cnt为当前m内可出现的组合的计数
            return cnt >= n 
        
        # range(min(nums) * n) 在 [0, a*n] 中二分查找
        # n 初始范围的下界
        # True 因为key写成了bool型，所以找最左边第一个满足 cnt>=n 的位置
            # 即目标是算出来第一个 key=True 的位置
        return bisect_left(range(min(nums) * n), True, n, key=check)
# @lc code=end

