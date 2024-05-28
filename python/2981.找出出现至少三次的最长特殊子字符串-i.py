#
# @lc app=leetcode.cn id=2981 lang=python3
#
# [2981] 找出出现至少三次的最长特殊子字符串 I
#
from collections import defaultdict
# @lc code=start
class Solution:
    def maximumLength(self, s: str) -> int:
        counter = defaultdict(int)
        lasti = 0
        length = 0
        result = 0
        for i, c in enumerate(s):
            if c == s[lasti]:
                length += 1
            else:
                tresult = result
                for j in range(tresult+1, length+1):
                    t = s[lasti] * j
                    counter[t] += length - j + 1
                    if counter[t] >= 3:
                        result = j
                lasti = i
                length = 1
        
        tresult = result
        for j in range(tresult+1, length+1):
            t = s[lasti] * j
            counter[t] += length - j + 1
            if counter[t] >= 3:
                result = j
        return result if result > 0 else -1
# @lc code=end

