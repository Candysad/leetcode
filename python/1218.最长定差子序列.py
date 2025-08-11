#
# @lc app=leetcode.cn id=1218 lang=python3
#
# [1218] 最长定差子序列
#
from collections import defaultdict
# @lc code=start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        '''
        动态规划，defaultdict(int)
        存每个位置能构成的最长序列，最后返回最长的
        '''
        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num-difference] + 1
            # 有就+1没有就会是0
            # 因为是从前往后遍历，一定是等差在前的元素先出现
            # dp是个字典，存的是之前出现的值和他们的最长距离
            # 对于当前数，等差数列中他前面的元素也一定会在它之前出现在arr里，也就会先出现在dp里
        
        return max(dp.values())
        
        '''
        重复数了太多次
        '''
        # counter = defaultdict(list)
        
        # for i, num in enumerate(arr):
        #     counter[num].append(i)
        
        # result = 0
        # for num in counter.keys():
        #     now_index = counter[num][0]
        #     now_result = 1
        #     now_num = num + difference
        #     while now_num in counter:
        #         save_index = now_index
        #         for t_index in counter[now_num]:
        #             if t_index > now_index:
        #                 now_result += 1
        #                 now_index = t_index
        #                 now_num += difference
        #                 break
        #         if now_index == save_index:
        #             break
            
        #     result = max(now_result, result)
        
        # return result
            
        
# @lc code=end

