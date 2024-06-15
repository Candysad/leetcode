#
# @lc app=leetcode.cn id=2800 lang=python3
#
# [2800] 包含三个字符串的最短字符串
#
from itertools import permutations
# @lc code=start
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        s = sorted([a, b, c])
        a, b, c = s
        
        if a in c and b in c: return c
        if a in b and c in b: return b
        if b in a and c in a: return a
        
        def generate(s):
            a, b, c = s
            result = a
            
            if b not in a:
                for i in range(len(b), -1, -1):
                    if result.endswith(b[:i]):
                        break
                result += b[i:]
                
            
            if c not in result:
                for i in range(len(result), -1, -1):
                    if result.endswith(c[:i]):
                        break
                result += c[i:]
            
            return result

        results = [generate(p) for p in permutations(s)]
        minl = len(min(results, key=lambda x: len(x)))
        
        result = 'z' * minl
        for r in results:
            if len(r) == minl and r < result:
                result = r
        return result 
# @lc code=end