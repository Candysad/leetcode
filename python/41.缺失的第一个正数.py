#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        需要先想到
        1.对于长度为n的nums
            最佳状态就是包含[1...n]，使得答案为n+1
            可推出一旦nums里出现负数或大于n的数，那么答案就会落在 [1,n] 里
        2.对于正负
            答案只看正数，所以所有数字的正负都无意义
            可以用原数组里每个数的正负号来表达信息
        3.结合1和2的结论
            可以在长度为n的数组里，用第i位的符号表示第i位是否已经出现过
            这样做需要先把符号都处理为同样的
            以负号表示i出现
                则先把所有负数变为正数，但是又不能影响原来的正数范围
                可以使用inf，或是n+1，因为一旦出现负数，答案就一定小于n+1了
            然后遍历一遍，把[1,n] 范围里出现的数用符号标记在对应位置
            最后遍历一遍找到第一个没出现的
        数组实际上的下标从0开始，所以1应该放在0里，整体往前挪1位
        '''
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n + 1
        
        for i, num in enumerate(nums):
            num = abs(num)
            if 0 < num < n + 1 and nums[num-1] > 0:
                nums[num-1] *= -1
        
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

        return n + 1
        '''
        开2^31-1个空间算不算常数个空间？
        用位和用数组一个意思，会爆内存
        '''
        # record = 0
        # for num in nums:
        #     if num > 0:
        #         record |= 1 << num
        
        # i = 1
        # if record:   
        #     record >>= 1
        #     while record:
        #         if record & 1 == 0:
        #             return i
        #         record >>= 1
        #         i += 1
        # return i
# @lc code=end

