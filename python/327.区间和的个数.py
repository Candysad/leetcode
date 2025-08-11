#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
from functools import cache
# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        存区间段内前缀和的个数
        存第二级的信息
        
        从前往后遍历前缀和，找前面出现过的在要求范围内的个数
        '''
        pres = [nums[0]]
        for num in nums[1:]:
            pres.append(num + pres[-1])
        
        vis = set()
        for pre in pres:
            vis.add(pre)
            vis.add(pre-lower)
            vis.add(pre-upper)
        vis = sorted(list(vis))
        n = len(vis)
        table = {pre : i+1 for i, pre in enumerate(vis)}
        
        fens = [0] * (n+1)
        def lowerbit(i):
            return i & -i
        
        def update(i, num):
            while i <= n:
                fens[i] += num
                i += lowerbit(i)
        
        def get(i):
            result = 0
            while i:
                result += fens[i]
                i -= lowerbit(i)
            return result
        
        result = 0
        for pre in pres:
            left, right = table[pre-upper], table[pre-lower]
            result += get(right) - get(left-1)
            update(table[pre], 1)
        return result
# @lc code=end

