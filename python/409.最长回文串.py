#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
from collections import Counter
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        result = 0
        odd = False
        for v in counter.values():
            if v % 2:
                odd = True
                result += v - 1   
            else:
                result += v
        
        return result if not odd else result + 1
# @lc code=end

