#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        以2个数为例，组合情况为
        00 01 10 11, 最大值为 2^n-1 = 3
        '''
        # n = len(nums)
        # t = 2**n
        
        # result = []
        # for i in range(t):
        #     r = []
        #     for j in range(n):
        #         if i >> j & 1:
        #           r.append(nums[j])
        #     result.append(r)
        
        # return result

        '''
        直接操作数组
        '''
        n = len(nums)
        result = [[]]
        for i in range(n):
            for j in range(len(result)):
                result.append(result[j] + [nums[i]])
        return result
        
# @lc code=end

