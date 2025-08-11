#
# @lc app=leetcode.cn id=1863 lang=python3
#
# [1863] 找出所有子集的异或总和再求和
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        枚举子集情况
        '''
        # length = len(nums)
        # result = 0
        # for i in range(1, 2**length): # 枚举所有子集
        #     t = 0
        #     for n in nums:
        #         t ^= n * (i & 1) # 按枚举的子集做异或
        #         i = i >> 1
        #     result += t
        # return result
        
        '''
        
        '''
        res=0
        for x in nums:
            res |= x
        return res<<(len(nums)-1)
# @lc code=end

