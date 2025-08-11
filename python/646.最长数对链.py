#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#
from collections import defaultdict
from heapq import *
# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        贪心+优先队列
        '''
        # rights = defaultdict(list)
        # for left, right in pairs:
        #     rights[right].append(left)
        
        # queue = [(k, rights[k]) for k in rights]
        # heapify(queue)
        
        # now = heappop(queue)[0]
        # result = 1
        
        # while queue:
        #     t_right, t_lefts = heappop(queue)
            
        #     if t_right <= now:
        #         continue
            
        #     for left in t_lefts:
        #         if left > now:
        #             result += 1
        #             now = t_right
        #             continue
        # return result
        
        '''
        动态规划
        dp[i] 为以 paris[i] 为末尾的最长长度
        比贪心慢
        '''
        n = len(pairs)
        dp = [1] * (n)
        pairs.sort()
        
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)        
# @lc code=end

