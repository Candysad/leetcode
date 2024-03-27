#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] 最长等差数列
#
from collections import defaultdict
# @lc code=start
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
        从前往后一次遍历
        爆内存..😓
        可以清除一些一定不是最长的选项来节省空间
        每一轮 剩下可能的最长长度 + 当前长度  <= 当前已有的最长
        删去这部分来节省内存
        
        还是爆内存...
        '''
        # n = len(nums)
        # queue = [(1, -1, nums[0])]
        
        
        # for i, num in enumerate(nums[1:]):
        #     t = queue
        #     t_max = 0
        #     for tt in queue:
        #         t_max = max(t_max, tt[0])
        #     queue = []
            
        #     for pre_q in t:
        #         if n-i + pre_q[0] > t_max:
        #             queue.append(pre_q)
        #         if pre_q[0] == 1:
        #             queue.append((2, num - pre_q[2], num))
        #         elif pre_q[1] == num - pre_q[2]:
        #             queue.append((pre_q[0] + 1, pre_q[1], num))
        #         else:
        #             queue.append(pre_q)
        #     queue.append((1, -1, num))
        #     print(queue)

        # t_max = 0
        # for q in queue:
        #     t_max = max(q[0], t_max)
        # return t_max 
        
        ''''
        动态规划
        转成 1218.定差子序列
        和1218的区别就是没给定差值，要自己遍历找
        '''
        diff = max(nums) - min(nums) # 只知道最大差，但并不知道max和min的前后，故差值也可能是min-max为负
        
        result = 2 # 至少有2个数
        for d in range(-diff, diff):
            dp = defaultdict(int)
            for num in nums:
                dp[num] = dp[num-d] + 1
            result = max(max(dp.values()), result)
        return result     
# @lc code=end

