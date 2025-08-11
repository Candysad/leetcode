#
# @lc app=leetcode.cn id=2981 lang=python3
#
# [2981] 找出出现至少三次的最长特殊子字符串 I
#
from collections import defaultdict, Counter
# @lc code=start
class Solution:
    def maximumLength(self, s: str) -> int:
        counter = defaultdict(list)
        lasti = 0
        for i, c in enumerate(s):
            if c != s[lasti]:
                length = i - lasti
                counter[s[lasti]].append(length)
                lasti = i
        counter[s[lasti]].append(len(s) - lasti)
        print(counter)
        
        result = -1
        for count in counter.values():
            tc = Counter(count)
            tk = sorted(list(tc.keys()))[-2:][::-1]
            print(tk)
            for i in range(len(tk)):
                length, c = tk[i], tc[length]
                
                if c + i*2 >= 3:
                    result = max(result, length)
                else:
                    result = max(result, length - 2)
                    if c > 1:
                        result = max(result, length - 1)

        return result if result > 0 else -1
# @lc code=end

