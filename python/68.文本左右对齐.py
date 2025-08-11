#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from itertools import zip_longest
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        stack = []
        nowl = 0
        for word in words:
            if stack:
                if nowl + 1 + len(word) > maxWidth:
                    result.append(stack)
                    stack = [word]
                    nowl = len(word)
                else:
                    stack.append(word)
                    nowl += 1 + len(word)
            else:
                stack.append(word)
                nowl += len(word)
        if stack:
            result.append(stack)
        
        def aspan(t:list):
            n = len(t)
            now = len(''.join(t))
            rest = maxWidth - now
            if rest == 0:
                return [0]
            
            if n == 1:
                blanks = [rest]
                return blanks
            
            blanks = [0] * (n-1)
            i = 0
            while rest:
                blanks[i] += 1
                rest -= 1
                i += 1
                i %= (n-1)
            return blanks
        
        for i, t in enumerate(result[:-1]):
            blanks = aspan(t)
            ts = zip_longest(t, blanks, fillvalue=0)
            r = [word + ' ' * v for word, v in ts]
            result[i] = ''.join(r)
        
        t = result.pop()
        r = ' '.join(t)
        r += " " * (maxWidth - len(r))
        result.append(r)

        return result    
# @lc code=end