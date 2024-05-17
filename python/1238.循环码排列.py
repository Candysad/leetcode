#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1238] 循环码排列
#

# @lc code=start
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        '''
        格雷码
        '''
        n = 2**n
        result = []
        si = 0
        for i in range(n):
            result.append(i ^ (i >> 1))
            if result[-1] == start:
                si = i
        
        return result[si:] + result[:si]
# @lc code=end