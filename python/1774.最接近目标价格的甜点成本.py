#
# @lc app=leetcode.cn id=1774 lang=python3
#
# [1774] 最接近目标价格的甜点成本
#
from collections import defaultdict
from bisect import bisect_left
# @lc code=start
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        '''
        配料一种能放最多2次
        基料至少放一种
        '''
        _sum = sum(toppingCosts)
        dp = defaultdict(int)
        dp[0] = 1
        toppingCosts.sort()
        
        for coin in toppingCosts:
            for i in range(2*_sum, coin-1, -1):
                dp[i] += dp[i-coin]
                dp[i+coin] += dp[i]
        
        result = defaultdict(int)
        for base in baseCosts:
            for key in dp:
                if dp[key] != 0:
                    result[base+key] += dp[key]
        result = sorted(list(result.keys()))
        
        i = bisect_left(result, target)
        if i == len(result):
            return result[-1]
        if result[i] == target: return target
        if i == 0: return result[0]
        
        tp = result[i-1]
        tb = result[i]
        return tp if abs(tp - target) <= abs(tb - target) else tb
# @lc code=end