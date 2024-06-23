#
# @lc app=leetcode.cn id=1717 lang=python3
#
# [1717] 删除子字符串的最大得分
#
from itertools import pairwise
from functools import reduce
# @lc code=start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s1, s2 = 'ab', 'ba'
        if x > y:
            x, y = y, x
            s1, s2 = s2, s1
        
        n = len(s)
        for start in range(n):
            if s[start] in 'ab': break
        spans = []
        for i in range(start, n):
            if s[i] not in 'ab':
                if start != -1:
                    if i - start >= 2 and 'a' in s[start:i] and 'b' in s[start:i]:
                        spans.append((start, i-1))
                    start = -1
            else:
                if start == -1:
                    start = i
        if start != -1:
            spans.append((start, n-1))

        def check(s):
            result = 0
            stack = []
            for c in s:
                if stack and stack[-1] + c == s2:
                    stack.pop()
                    result += y
                else:
                    stack.append(c)
            
            s = ''.join(stack)
            stack = []
            for c in s:
                if stack and stack[-1] + c == s1:
                    stack.pop()
                    result += x
                else:
                    stack.append(c)
            return result
        
        result = 0
        for i, j in spans:
            result += check(s[i:j+1])
        return result         
# @lc code=end

