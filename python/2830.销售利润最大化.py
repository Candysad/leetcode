#
# @lc app=leetcode.cn id=2830 lang=python3
#
# [2830] 销售利润最大化
#
from functools import cache
from collections import defaultdict
# @lc code=start
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        '''
        树状数组
        '''
        # offers.sort()
        # keys = set()
        # for left, right, _ in offers:
        #     keys.add(left-1)
        #     keys.add(right)
        # keys = { key : i+1 for i, key in enumerate(sorted(list(keys)))}
        # m = len(keys)
        
        # tree = defaultdict(int)
        # def lowerbit(i):
        #     return i & (-i)
        
        # def update(i, num):
        #     while i <= m:
        #         if num > tree[i]: 
        #             tree[i] = num
        #             i += lowerbit(i)
        #         else: break
        
        # def find(i):
        #     result = 0
        #     while i:
        #         result = max(result, tree[i])
        #         i -= lowerbit(i)
        #     return result

        # for left, right, gold in offers:
        #     lefti = keys[left - 1]
        #     pre = find(lefti)
            
        #     righti = keys[right]
        #     update(righti, gold + pre)
        # return find(m)

        '''
        DP
        '''
        dp = [0] * (n + 1)
        t = defaultdict(list)
        for left, right, gold in offers:
            t[right].append((left, right, gold))
        offers = t
        
        result = 0
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for left, right, gold in offers[i-1]:
                dp[i] = max(dp[i], dp[left] + gold)
            result = max(result, dp[i])
        return result   
# @lc code=end