#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#
from collections import defaultdict
# @lc code=start
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        table = {c:i+1 for i, c in enumerate(cost)}
        coins = sorted(list(table.keys()))
        
        def comp(l1, l2):
            if l1[-1] > l2[-1]: return l1
            elif l1[-1] < l2[-1]: return l2
            
            for i in range(8, -1, -1):
                if l1[i] > l2[i]:
                    return l1
                elif l1[i] < l2[i]:
                    return l2
            return l1
        
        dp = [[0] * 10]
        for i in range(1, target+1):
            now = [0] * 9 + [-1]
            for coin in coins:
                if i < coin: break
                if dp[i-coin][-1] == -1: continue
                t = dp[i-coin].copy()
                num = table[coin]
                t[num-1] += 1
                t[-1] += 1
                now = comp(now, t)
                
            dp.append(now)

        if dp[-1][-1] == -1: return '0'
        result = []
        for i in range(8, -1, -1):
            result.append(str(i+1) * dp[-1][i])
        result = ''.join(result)
        return result
# @lc code=end