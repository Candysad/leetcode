#
# @lc app=leetcode.cn id=616 lang=python3
#
# [616] 给字符串添加加粗标签
#

# @lc code=start
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        spans = []
        for i in range(n):
            for word in words:
                if s[i:].startswith(word):
                    spans.append((i, i+len(word)-1))
        if not spans: return s
        spans.sort()
        
        result = []
        left, right = spans[0]
        for i in range(1, len(spans)):
            if right >= spans[i][0]-1:
                right = max(right, spans[i][1])
            else:
                result.append((left, right))
                left, right = spans[i]
        result.append((left, right))
        
        r = []
        j = 0
        spn = len(result)
        for i in range(n):
            if j < spn and i == result[j][0]:
                r.append('<b>')
            
            r.append(s[i])
            
            if j < spn and i == result[j][1]:
                r.append('</b>')
                j += 1
        return ''.join(r)        
# @lc code=end