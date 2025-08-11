#
# @lc app=leetcode.cn id=1363 lang=python3
#
# [1363] 形成三的最大倍数
#
from collections import defaultdict
# @lc code=start
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        table = defaultdict(list)
        zeros = 0
        for d in digits:
            if d == 0:
                zeros += 1
            else:
                table[d % 3].append(d)
        
        table[1].sort()
        table[2].sort()
        n1, n2 = len(table[1]), len(table[2])
        t1, t2 = table[1], table[2]
        if n1 < n2:
            n1, n2 = n2, n1
            t1, t2 = t2, t1
        
        t = (n1-n2) % 3
        p1, p2 = n1-n2, 0
        if t == 0:
            p1 = 0
        elif t == 1:
            p1 = 1
        elif t == 2:
            if n2 >= 1:
                p1 = 0
                p2 = 1
            else:
                p1 = 2
        
        result = table[0] + t1[p1:] + t2[p2:]
        result.sort()
        result = ''.join(str(c) for c in result[::-1]) + "0" * zeros
        return "0" if result.startswith('0') else result
# @lc code=end

