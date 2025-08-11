#
# @lc app=leetcode.cn id=1156 lang=python3
#
# [1156] 单字符重复子串的最大长度
#

# @lc code=start
'''
滑动窗口

考虑
两个隔一个的区间连起来
或有更多的区间的时候补在隔一个的两个区间中间
或新来一个特别长但是离前面特别远的
'''
class Span():
    def __init__(self) -> None:
        self.spans = []
        self.count = 0
        self.max_length = 0
        self.potential_max = 0
        

    def update(self, span:list):
        self.spans.append(span)
        self.count += 1
        
        if self.count == 1: # 就一个区间
            self.max_length = self.spans[0][1] - self.spans[0][0] + 1
        elif self.count == 2: # 两个区间
            span1 = self.spans[0]
            len1 = span1[1] - span1[0] + 1 
            span2 = self.spans[1]
            len2 = span2[1] - span2[0] + 1
            
            if span1[1] + 2 == span2[0]: # 看能不能连起来
                # 万一还有下一个，可以填一个在中间全连起来还+1
                self.potential_max = max(self.potential_max, len1 + len2 + 1)
                self.max_length = len1 + len2
            else:
                self.max_length = max(len1+1, len2+1)
        
        else: # 多余两个区间
            span1 = self.spans[-2]
            len1 = span1[1] - span1[0] + 1 
            span2 = self.spans[-1]
            len2 = span2[1] - span2[0] + 1
            if span1[1] + 2 == span2[0]: # 看会不会新填进去连起来更长
                self.potential_max = max(self.potential_max, len1 + len2 + 1)
            
            # 新来的连不起来但是特别长，或者把最长的缺一个的连起来
            self.max_length = max(self.max_length, len2+1, self.potential_max)
        
        return self.max_length
         
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        table = {}
        lasti = 0
        lastc = text[0]
        result = 1
        for i, c in enumerate(text):
            # 还在连续区间里
            if c == lastc: continue
            
            # 脱离区间
            span = [lasti, i-1]
            if lastc not in table:
                table[lastc] = Span()
            result = max(table[lastc].update(span), result)
            
            # 更新遍历
            lastc = c
            lasti = i
            print(result)
        
        span = [lasti, n-1]
        if lastc not in table:
            table[lastc] = Span()
        result = max(table[lastc].update(span), result)
        print(result)
        
        for v in table.values():
            print(v.spans)
            print(v.max_length)
            
        return result
# @lc code=end

