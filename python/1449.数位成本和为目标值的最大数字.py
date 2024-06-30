#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#
from collections import defaultdict
# @lc code=start
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        table = defaultdict(int)
        for i, c in enumerate(cost):
            table[c] = i + 1
        coins = list(table.keys())
        
        def comp(s1, s2):
            l1, l2 = len(s1), len(s2)
            if l1 > l2: return s1
            elif l1 < l2: return s2
            return max(s1, s2)
        
        dp = [None for _ in range(target+1)]
        dp[0] = []
        
        for i in range(1, target + 1):
            for coin in coins:
                if i >= coin and dp[i-coin] != None:
                    t = dp[i-coin].copy()
                    t.append(table[coin])
                    t.sort(reverse=True)
                    if dp[i] == None:
                        dp[i] = t
                    else:
                        dp[i] = comp(dp[i], t)
        
        result = dp[-1]
        return ''.join([str(c) for c in result]) if result is not None else '0'
# @lc code=end