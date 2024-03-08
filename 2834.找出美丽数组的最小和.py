#
# @lc app=leetcode.cn id=2834 lang=python3
#
# [2834] 找出美丽数组的最小和
#

# @lc code=start
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        '''
        贪心
        先不考虑target，最小和的序列就是1开始的自然数，共n个
        分类讨论k和n的关系
        从加和为target的大的一侧的第一个数开始集体往右挪
        在原本序列的和上 加上 加和为target的组 的组数*右移的距离
        
        右移太复杂，本质证明了：
        就是小于target一半的数加上从target开始的剩余个数的两个序列的和
        '''
        mod = 10**9 + 7
        t = target // 2
        if n <= t:
            return (1 + n) * n // 2 % mod
        
        return ((1 + t) * t // 2 + (target + target + n - t +  - 1) * (n - t) // 2) % mod
# @lc code=end

