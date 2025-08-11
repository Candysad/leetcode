#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
from math import factorial
# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        result = []
        
        def abit(bit:int, k:int) -> int: # bit 指出当前是从低到高第几位
            unit = factorial(bit-1)
            
            base = (k-1) // unit
            k -= base * unit
            
            num = nums[base]
            nums.remove(num)
            
            return num, k
        
        for i in range(n, 1, -1):
            num, k = abit(i, k)
            result.append(num)
        result.append(nums[-1])
        
        return ''.join(map(str, result))
# @lc code=end

