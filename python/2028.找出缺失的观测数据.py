#
# @lc app=leetcode.cn id=2028 lang=python3
#
# [2028] 找出缺失的观测数据
#

# @lc code=start
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m, pre = len(rolls), sum(rolls)
        _sum = (m + n) * mean
        _sum -= pre
        
        print(_sum, n*6)
        if _sum > n * 6 or _sum < n:
            return []
        
        mean = _sum // n
        t = _sum % n
        return [mean+1] * t + [mean] * (n-t)  
# @lc code=end