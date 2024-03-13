#
# @lc app=leetcode.cn id=2864 lang=python3
#
# [2864] 最大二进制奇数
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1"*(sum([1 if c == '1' else 0 for c in s])-1) + "0"*(len(s)-sum([1 if c == '1' else 0 for c in s]))  + "1"
        
# @lc code=end

